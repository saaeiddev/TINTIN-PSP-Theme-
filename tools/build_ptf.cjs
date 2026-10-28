// Uses the unmodified PTF Studio 1.0 encoder and parser from its checked-out
// app.js. See README for the pinned upstream commit and GPL-3.0 license.
const fs = require('fs');
const path = require('path');
const { PNG } = require('pngjs');
const root = path.resolve(__dirname, '..');
const studioPath = process.env.PTF_STUDIO_DIR;
if (!studioPath) throw new Error('Set PTF_STUDIO_DIR to a checkout of PTF Studio 1.0.');
const code = fs.readFileSync(path.join(studioPath, 'app.js'), 'utf8');
const take = (start, end) => {
  const a = code.indexOf(start), b = code.indexOf(end, a);
  if (a < 0 || b < 0) throw new Error(`Expected PTF Studio functions are missing: ${start}`);
  return code.slice(a, b);
};
const source = [
  take('function readFixedString', 'function currentProfile'),
  take('async function parsePtf', 'function countColors'),
  take('const PSP_FOCUS_MARGIN', 'function focusOptionsFromUi'),
  take('function quantize(imageData', 'function normalizeExportFileName'),
].join('\n');
const prelude = `
const window = globalThis;
const CATEGORY_LABELS = {1:'Settings',2:'Photo',3:'Music',4:'Video',5:'TV',6:'Game',7:'Network',8:'Extras'};
const FIRST_LABELS = {};
const PTF_FIRST_LEVEL_MAX_SUB = 59;
const els = { ditherToggle:{checked:false}, themeName:{value:'Tintin'}, productId:{value:'TINTIN_PSP'}, version:{value:'1.0'}, themeColor:{value:'0'} };
const state = { theme:{pspVersion:'6.20',value8:8}, assets:[] };
class ImageData { constructor(data,width,height){this.data=data;this.width=width;this.height=height;} }
`;
const run = `
function png(file){ const p=PNG.sync.read(fs.readFileSync(path.join(root,file))); return {width:p.width,height:p.height,data:new Uint8ClampedArray(p.data)}; }
function add(objIdx,subIdx,fileType,imageData,focus=false){ const role=roleFor(objIdx,subIdx); state.assets.push({objIdx,subIdx,fileType,role,imageData,edited:true,comp:2,pspGeneratedFocus:focus}); }
function find(folder,prefix){ const items=fs.readdirSync(path.join(root,folder)).filter(f=>f.startsWith(prefix+'-') && f.endsWith('.png')); if(items.length!==1)throw new Error('Expected exactly one '+folder+'/'+prefix); return folder+'/'+items[0]; }
async function main(){
 add(0,0,5,png('assets/preview/icon.png'));
 add(0,1,5,png('assets/preview/preview.png'));
 add(1,0,4,png('assets/wallpaper.png'));
 for (const [slot,name] of Object.entries({1:'settings',2:'photo',3:'music',4:'video',5:'tv',6:'game',7:'network',8:'extras'})) add(2,Number(slot),5,png('assets/icons/category/'+name+'.png'));
 for(let slot=2;slot<=58;slot+=2){let p=String(slot).padStart(2,'0'); add(3,slot,5,png(find('assets/icons/first-level',p))); add(3,slot+1,5,png(find('assets/icons/first-focus',p)),true);}
 for(const slot of [0,2]){let p=String(slot).padStart(2,'0'); add(4,slot,5,png(find('assets/icons/second-level',p))); add(4,slot+1,5,png(find('assets/icons/second-focus',p)),true);}
 const built=await buildPtf({status:false,title:'TINTIN PSP Theme',productId:'TINTIN_PSP',version:'1.0',themeColor:0});
 verifyBuiltPtfMetadata(built.bytes,{title:'TINTIN PSP Theme',productId:'TINTIN_PSP',version:'1.0',themeColor:0});
 if(built.bytes.length>768*1024)throw new Error('PTF exceeds PTF Studio 768 KiB limit');
 const parsed=await parsePtf(built.bytes.buffer,'TINTIN_PSP_Theme.ptf');
 if(parsed.assets.length!==73)throw new Error('Unexpected PTF asset count: '+parsed.assets.length);
 for(const a of parsed.assets){
   if(a.fileType===4){ if(a.rawOriginal[0]!==66 || a.rawOriginal[1]!==77)throw new Error('Bad wallpaper BMP'); continue; }
   if(a.decodeError)throw new Error('Failed to decode '+a.objIdx+':'+a.subIdx+': '+a.decodeError);
   if(a.imageData.width!==a.role.required[0]||a.imageData.height!==a.role.required[1])throw new Error('Bad dimensions '+a.objIdx+':'+a.subIdx);
   if(a.role.indexed && a.paletteCount>256)throw new Error('Palette too large');
 }
 fs.mkdirSync(path.join(root,'release'),{recursive:true});
 fs.writeFileSync(path.join(root,'release/TINTIN_PSP_Theme.ptf'),built.bytes);
 console.log(JSON.stringify({size:built.bytes.length,decoded:parsed.assets.length,stats:built.stats},null,2));
}
return main();
`;
new Function('fs','path','PNG','root',prelude+source+run)(fs,path,PNG,root).catch(e=>{console.error(e);process.exit(1)});
