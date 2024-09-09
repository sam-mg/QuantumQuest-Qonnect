#!/usr/bin/python3

from Crypto.Cipher import AES
import hashlib
import random
from requests.api import get

def getct():
	con = get(f'https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
	out = bytes.fromhex(con.json()['ciphertext'])
	return out

def decct(ct, pwd):
	
	cipher = AES.new(pwd, AES.MODE_ECB)
	try:
		decrypted = cipher.decrypt(ct)
	except ValueError as e:
		return {"error": str(e)}

	return decrypted


with open("words") as f:
    words = [w.strip() for w in f.readlines()]

ct = getct()

for i in words:	
	KEY = hashlib.md5(i.encode()).digest()
	pt_c = decct(ct, KEY)
	if b'crypto' in pt_c:
		print(pt_c)
