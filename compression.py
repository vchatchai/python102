import zlib

s = b'witch which has which witches wrist watch'
print( f's={s}')
print(f'len(s) => {len(s)}')

t = zlib.compress(s)
print(f'len(zlib.compress(s) => {len(t)}')

b = zlib.decompress(t)
print(f'zlib.decompress(t) => {b}')

print(f'zlib.crc32(s) => {zlib.crc32(s)}')