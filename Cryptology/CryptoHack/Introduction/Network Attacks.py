#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

r = remote("socket.cryptohack.org", 11112)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "flag"
}

json_send(request)
response = json_recv()

print(response)