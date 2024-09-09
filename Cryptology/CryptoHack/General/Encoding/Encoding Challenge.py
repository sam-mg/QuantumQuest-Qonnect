from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
	print("#######", hsh)
	request = json.dumps(hsh).encode()
	r.sendline(request)

def decoded(tpe, ct):
	if tpe == "base64":
		pt = base64.b64decode(ct.encode()).decode()
	elif tpe == "hex":
		pt = bytes.fromhex(ct).decode()
	elif tpe == "rot13":
		pt = codecs.decode(ct, "rot_13")
	elif tpe == "bigint":
		pt = long_to_bytes(int(ct, 16)).decode()
	elif tpe == "utf-8":
		pt = "".join([chr(i) for i in ct])
	return pt

for i in range(100):
	received = json_recv()

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	a = decoded(received["type"], received["encoded"])
	to_send = {
		"decoded": a
	}
	json_send(to_send)

json_recv()