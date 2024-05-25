Let's move forward to the next level!

![untitled](ScreenShots/Level%2031%20->%2032.jpg)

There is something we need to escape. Let's find out what it is.

---
First, log in to look into the upcoming challenge.  
This challenge converts everything we enter into uppercase characters.

When we research this issue, we find this useful command on [COMMANDLINEFU](https://www.commandlinefu.com/commands/view/11704/launch-bash-without-using-any-letters).

Using `$0`, we can exit the uppercase mode.  
Once we escape it, we can retrieve the password from the `/etc/` directory with the following command:
```bash
cat /etc/bandit_pass/bandit33
```
After obtaining the password, we can disconnect and connect to the next level using these commands:
```bash
Command: `ssh -p 2220 bandit33@bandit.labs.overthewire.org`
#Password: Retrieved from /etc/bandit_pass/ directory
```
<!-- Password: `odHo63fHiFqcWWJG9rLiLDtPm45KzUKy` -->