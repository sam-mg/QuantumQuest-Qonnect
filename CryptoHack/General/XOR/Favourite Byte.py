from pwn import xor
a = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for i in range(129):
    if b'crypto' in xor(a,i):
        print(xor(a,i))