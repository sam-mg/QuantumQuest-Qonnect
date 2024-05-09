Let's now advance to the next level.

![untitled](ScreenShots/Level%2014%20->%2015.jpg)

It has been indicated that the password for the subsequent level can be retrieved by submitting the password of the current level on `port 30000` of `localhost`.

---
**How to Connect to Different Ports?**
- Utilize the guidance provided in [Level 0](https://github.com/sam-mg/OverTheWire/blob/main/Bandit/Level%20-%200.md).
- Refer to the documentation on [tutorialspoint](https://www.tutorialspoint.com/the-netcat-command-in-linux) for further insights.
- Additionally, explore resources from [SCALAR Topics](https://www.tutorialspoint.com/the-netcat-command-in-linux) for comprehensive understanding.

---
From these references, we can deduce the following command:
```bash
nc localhost 30000
```
and then input the password of the previous level.
<p align="center">(alternatively)</p>

```bash
cat /etc/bandit_pass/bandit14 | nc localhost 30000
```
Both methods yield the same flag.

Once obtained, we can progress to the next level using the following commands:
```bash
Command: `ssh -p 2220 bandit15@bandit.labs.overthewire.org`
#Password: The password retrieved from the previous connection
```
<!-- Password: `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt` -->