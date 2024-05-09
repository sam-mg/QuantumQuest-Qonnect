Let's delve into the next stage, progressing from level 10 to 11.

![untitled](ScreenShots/Level%2010%20->%2011.jpg)

The directive is clear: the password resides within a file, but it's obscured using base64 encoding.

---
**Decoding Base64:**
- Utilizing online platforms such as [Base64 Decode](https://www.base64decode.org/), [Base64decode](https://www.base64decode.net/), [RapidTables](https://www.base64decode.net/)
- Executing terminal commands, referencing resources like [Medium](https://medium.com/@IToolkit_co/how-to-base64-decode-on-mac-baa30cc15b0c), [HACKERNOON](https://hackernoon.com/how-to-convert-base64-data-to-files-on-linux-and-mac-os), [Ask Ubuntu](https://askubuntu.com/questions/178521/how-can-i-decode-a-base64-string-from-the-command-line)
- Crafting a Python solution tailored to your needs

---
Let's explore the available methods:
1. Python Script:
    ```python
    import base64
    with open("data.txt", "r") as file:
        text = file.read()
    decoded_text = base64.b64decode(text).decode().strip()
    print(decoded_text)
    ```
2. Terminal Commands:
    ```bash
    base64 -d -i data.txt
    ```
Both methods yield the same decrypted text.  

Once we acquire the password, we can exit the SSH and proceed to the next level using the following commands:
```bash
Command: `ssh -p 2220 bandit11@bandit.labs.overthewire.org`
#Password: Extracted from the Base64-encoded text
```
<!-- Password: `6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM` -->