Let's take a closer look at the transition from Level 26 to Level 27.

![untitled](ScreenShots/Level%2026%20->%2027.jpg)

The task is to quickly find the password.

---
We notice that the logout mechanism is the same as the previous level. Therefore, we will follow the same steps we used before.
First, set the shell to `/bin/bash` by using the following command:
```bash
:set shell=/bin/bash
```
Once the shell is set, we can access it using:
```bash
:sh
```
After gaining shell access, we use `ls` to list the contents of the directory. We notice the presence of a `Setuid` file.
Let's proceed similarly to [Level 19 -> 20](https://github.com/sam-mg/OverTheWire/blob/main/Bandit/Level%2019%20-%3E%2020.md)

Upon retrieving the password, log out of the current SSH session and connect to the next level using the following command:
```bash
Command: `ssh -p 2220 bandit26@bandit.labs.overthewire.org`
#Password: Retrieved from the /etc/bandit_pass/ directory
```
<!-- Password: `YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS` -->