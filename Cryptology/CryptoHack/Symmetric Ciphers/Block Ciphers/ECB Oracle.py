#!/usr/bin/python3

from Crypto.Cipher import AES
from string import printable

import requests

def vuln(a):
	print(a)
	out = bytes.fromhex(requests.api.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{a.hex()}/').json()['ciphertext'])
	print(out)
	return out

CSTR = str(printable)

def pad(inp, ln=16):
    k = ln - (len(inp)%16)
    return inp+bytes([k]*k)

def spliter(txt):
    return [txt[i:i+16] for i in range(0, len(txt), 16)]

# Attack Methodology.
def attack():
    # Step 1 - Find the location where attack should happen.
    # ie - Block 1, 2, .., N?
    # This is because there might be some data prior to the
    # input data.
    nvuln = check(vuln)
    if not nvuln: return nvuln

    # Step 2 - Find the length of the secret string.
    prev = len(nvuln(b""))
    bseln = find_len(prev, nvuln)
    if bseln == -1: return None

    # Step 3 - For loop for each character to find. And
    # search for a matching cipher.
    return brute(prev, bseln, nvuln)

def brute(prev, bseln, nvuln):
    # A function to brute force for all possible input
    # values for the encryption.
    knw = b""
    for i in range(1, (prev*16)-bseln+1):
        val = nvuln(b"a"*(bseln+i))[prev]
        for j in CSTR:
            inp = spliter(pad(j.encode()+knw))[0]
            if nvuln(inp)[0] == val:
                break
        knw = j.encode()+knw
    return knw

def find_len(prev, nvuln):
    # A function to find the length of the secret in text
    for i in range(1,16):
        ret = nvuln(b"a"*i)
        if len(ret)!=prev:
            return i

    return -1

def check(vuln):
    # Makes and returns function that adjusts the input &
    # output so that it feels like you are inputting info
    # at location 0.
    a = spliter(vuln(b"a"))
    b = spliter(vuln(b"b"))
    i = 0
    while a[i] == b[i]:
        i+=1

    fl = spliter(vuln(b"a"*16))[i]
    for j in range(15, -1, -1):
        if fl != spliter(vuln(b"a"*j))[i]:
            return lambda a: spliter(vuln((b"a"*(j+1))+a))[i+1:]
    return None

if __name__=="__main__":
    print(attack().decode())