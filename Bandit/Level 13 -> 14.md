Let's elevate our focus to the next tier of challenge.

![untitled](ScreenShots/Level%2013%20->%2014.jpg)

In this intriguing challenge, the task is straightforward yet requires precision: to unveil the password for accessing the next level.  
The password lies dormant within `/etc/bandit_pass/bandit14`, tantalizingly out of reach except for the eyes of bandit14.  
To unlock this secret vault, we are armed with a key, a `sshkey.private` file, granting us passage to bandit14's domain.

---
**Navigating SSH: A Recap**
- Recall our initial encounter with SSH and its mechanics back in [Level 0](https://github.com/sam-mg/OverTheWire/blob/main/Bandit/Level%20-%200.md).

---
With this knowledge in tow, the path ahead unfolds.  
Our command, succinct yet powerful, orchestrates our connection:
```bash
ssh bandit14@localhost -i sshkey.private -p 2220
```
Upon executing this command, the gateway beckons for authentication.  
Fear not; a simple affirmation, typing `yes`, clears the way forward.  
As we traverse into the realm of bandit14, the repository of secrets reveals itself within `/etc/bandit_pass/bandit14`.  
To claim our prize, we invoke the command:
```bash
cat /etc/bandit_pass/bandit14
```
With the password now unveiled, our mission concludes.  

A swift exit paves the way for our ascent to the next echelon, facilitated by these commands:
```bash
Command: `ssh -p 2220 bandit14@bandit.labs.overthewire.org`
#Password: Extracted from the specified directory file
```
<!-- Password: `wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw` -->