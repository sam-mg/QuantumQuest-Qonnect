from pwn import xor
a = bytes.fromhex('2b17002f00071e1f1c0007123204001a1d3e180b30061e00091638054e4e550e')
b = b'hey_there_is_a_snake_in_my_boots'
d = b'Crypto{my_name_is_snoop_dogg!!!}'
for i in range(128):
	c = b + bytes([i])
	print(xor(a,d))