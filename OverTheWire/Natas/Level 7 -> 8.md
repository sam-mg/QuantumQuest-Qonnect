Let's delve into the next level using the credentials we obtained from the previous stage.

Upon logging in, we encounter a similar interface as seen in `natas7`.
![untitled](ScreenShots/Level%207%20->%208.jpg)

---
Inspecting the source code reveals the following PHP script:
```php
<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
?>
```
For those unfamiliar with PHP, here is an equivalent representation in Python:
```py
encoded_secret = "3d3d516343746d4d6d6c315669563362"
def encode_secret(secret):
    return hex(int.from_bytes(secret.encode()[::-1], byteorder='big'))
```

To decipher the encoded secret, we can use a reverse Python script:
```py
import base64
required = "3d3d516343746d4d6d6c315669563362"
def decode_secret(secret):
    return base64.b64decode(bytes.fromhex(secret).decode("ASCII")[::-1]).decode()
print(decode_secret(required))
```
Executing this script provides the secret key required to retrieve the password for the next level.

Armed with this information, we can now access the subsequent level using the following credentials:
```
URL: http://natas9.natas.labs.overthewire.org
Username: natas9
Password: Password obtained by entering the secret key
```
<!-- Password: `Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd` -->