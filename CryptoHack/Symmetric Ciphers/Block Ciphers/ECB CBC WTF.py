#!/usr/bin/python3

from requests.api import get
from pwn import xor

def spliter(txt):
    return [txt[i:i+16] for i in range(0, len(txt), 16)]
    
def decct(ct):
	con = get(f'https://aes.cryptohack.org/ecbcbcwtf/decrypt/{ct.hex()}/')
	out = bytes.fromhex(con.json()['plaintext'])
	return out

def getct():	
	con = get(f'https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
	out = bytes.fromhex(con.json()['ciphertext'])
	return out

ct = getct()
ct_splited = spliter(ct)

for i in range(1, len(ct_splited)):
	pt = decct(ct_splited[i])
	iv = ct_splited[i-1]
	pt_1 = xor(pt, iv).decode()
	print(pt_1,end='')
