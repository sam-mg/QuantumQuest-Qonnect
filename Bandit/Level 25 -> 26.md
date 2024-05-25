Let's delve into the next level of this challenge.

![untitled](ScreenShots/Level%2025%20->%2026.jpg)

Our task is to log into level 26 using the provided `sshkey`. However, the twist is that a different shell is used instead of the usual `/bin/bash`.

---
**What is the `more` command?**
- Referencing from [GeeksforGeeks](https://www.geeksforgeeks.org/more-command-in-linux-with-examples/)
- Also from [Livewire](https://www.lifewire.com/more-command-4041467)
- Additionally from [scaler](https://www.scaler.com/topics/more-command-in-linux/)
- Furthermore from [man7](https://man7.org/linux/man-pages/man1/more.1.html)
- The best option is to use `man more` to view detailed information about the `more` command.
---
Now, let's explore how this level behaves when we use the provided sshkey with the following command:
```bash
ssh -i bandit26.sshkey bandit26@localhost -p 2220
```
Once you log in, you'll notice that it logs out automatically.

![untitled](ScreenShots/Level%2025%20->%2026%20(Terminal).jpg)

The description indicates that a different shell is used. We can identify the shell by using this command:
```bash
cat /etc/passwd | grep "bandit"
```
This command allows us to see the shells used by different levels. For level 26, we find:
```bash
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```
The shell appears to be a text file. Let's examine it:
```sh
#!/bin/sh
export TERM=linux
exec more ~/text.txt
exit 0
```
From this script, we see that the `more` command is used to view a file according to the terminal's dimensions. By pressing `enter`, the content continues, and pressing `v` opens the editor at the current line. To view the password for the next level, we can use:
```bash
:e /etc/bandit_pass/bandit26
```
This will display the password.

After obtaining the password, exit the SSH session and connect to the next level using:
```bash
Command: `ssh -p 2220 bandit26@bandit.labs.overthewire.org`
#Password: Password obtained from the shell to proceed.
```
<!-- Password: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1 -->