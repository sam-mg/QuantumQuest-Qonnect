#!/usr/bin/python3

import telnetlib
import json


server = telnetlib.Telnet("socket.cryptohack.org", 13372)

def readline():
    return server.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(flag):
    rq = json.dumps(flag).encode()
    server.write(rq)

print(readline())
json_send({"option": "get_flag"})
received = json_recv()

input = received["encrypted_flag"]
json_send({"option": "encrypt_data","input_data": input})
received = json_recv()

flag = received["encrypted_data"]
print(flag)
flag = bytes.fromhex(flag)
print(flag)
