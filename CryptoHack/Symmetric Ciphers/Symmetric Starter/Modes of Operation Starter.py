#!/usr/bin/python3

from requests.api import get
   
def decct(ct):
	con = get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{ct.hex()}/')
	out = bytes.fromhex(con.json()['plaintext'])
	return out

def getct():	
	con = get(f'https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
	out = bytes.fromhex(con.json()['ciphertext'])
	return out

ct = getct()
pl = decct(ct)

print(bytes(pl))