#!/usr/bin/env python3
"""Independent structural checks for the project's PTF container and resources."""
import hashlib, struct, sys, zlib
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'release/TINTIN_PSP_Theme.ptf'
d = p.read_bytes()
assert 0 < len(d) <= 768 * 1024 and d[:8] == b'\0PTF\0\x01\0\0'
assert d[8:136].split(b'\0')[0] == b'TINTIN PSP Theme'
assert d[136:184].split(b'\0')[0] == b'TINTIN_PSP'
u16 = lambda o: struct.unpack_from('<H', d, o)[0]
u32 = lambda o: struct.unpack_from('<I', d, o)[0]
seen = {}
for group_offset in struct.unpack_from('<8I', d, 0x100):
    if not group_offset: continue
    assert group_offset + 32 <= len(d)
    group, count, length, pos = struct.unpack_from('<HHII', d, group_offset)
    assert pos == group_offset + 32 and pos + length <= len(d)
    end = pos + length
    for _ in range(count):
        assert pos + 32 <= end
        sub, _, typ, compression, size, uncompressed = struct.unpack_from('<HHHHII', d, pos)
        assert size % 4 == 0 and pos + 32 + size <= end
        data = d[pos+32:pos+32+size]
        raw = zlib.decompress(data) if compression == 2 and size < uncompressed else data[:uncompressed]
        assert len(raw) == uncompressed and (group,sub) not in seen
        seen[group,sub] = (typ, raw)
        pos += 32 + size
    assert pos == end
assert set(g for g,s in seen) == {0,1,2,3,4}
assert len(seen) == 74
assert seen[0,2] == (5, b'\0\0\0\0')
typ, bmp = seen[1,0]
assert typ == 4 and bmp[:2] == b'BM'
assert struct.unpack_from('<ii',bmp,18) == (480,272) and struct.unpack_from('<H',bmp,28)[0] == 24
expected = {(0,0):(16,16),(0,1):(300,170)}
expected.update({(2,i):(64,48) for i in range(1,9)})
expected.update({(3,i):((48,48) if i%2==0 else (64,64)) for i in range(2,60)})
expected.update({(4,i):((32,32) if i%2==0 else (48,48)) for i in range(4)})
assert set(expected) == set(seen)-{(0,2),(1,0)}
for key, dimensions in expected.items():
    typ, raw = seen[key]
    assert typ == 5 and raw.startswith(b'MIG.00.1PSP\0')
    pos, blocks, image = 16, [], None
    while pos+16 <= len(raw):
        block, _, size, nextpos, _ = struct.unpack_from('<HHIII',raw,pos)
        assert size >= 16 and pos+size <= len(raw)
        if block in (4,5):
            fmt, order, w, h, bpp = struct.unpack_from('<HHHHH',raw,pos+20)
            blocks.append((block,fmt,w,h,bpp))
            if block == 4: image=(w,h,bpp)
        if not nextpos: break
        assert nextpos >= 16
        pos += nextpos
    assert image is not None and image[:2] == dimensions, (key,image,dimensions)
    if key != (0,1):
        assert image[2] == 8 and any(b[0]==5 and b[2]==256 for b in blocks), (key,blocks)
    else: assert image[2] == 32
print(f'PASS: {len(seen)} records; 73 image resources; GIM/BMP dimensions checked; {len(d)} bytes')
print('SHA-256:',hashlib.sha256(d).hexdigest())
