import hashlib

with open ('/Users/sammgharish/Desktop/Cryptology/CryptoHack/RSA/Starter/RSA_Starter_6-Private_Key.key' , 'r') as data:
    file = data.readlines()

data = []
for i in file:
    a = i.split()
    data.append([b.strip() for b in a])

n = int(data[0][-1])
d = int(data[-1][-1])

flag = b"crypto{Immut4ble_m3ssag1ng}"
hash_value = hashlib.sha256(flag).digest()

hash_int = int.from_bytes(hash_value, 'big')

print(pow(hash_int, d, n))