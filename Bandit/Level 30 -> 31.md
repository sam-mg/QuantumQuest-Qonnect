Let's move on to the next level.

![untitled](ScreenShots/Level%2030%20->%2031.jpg)

To advance, we need to retrieve the password stored in the provided repository.  
While this step is slightly more complex than the previous one, it is manageable with a systematic approach.

---
**What is `git tag`?**
-  Referencing from [Git-SCM](https://git-scm.com/docs/git-tag)
---
First, we need to create a directory in the `/tmp/` folder and clone the repository using the following commands:
```bash
mkdir /tmp/bandit28/
cd /tmp/bandit28/
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
```
Although we can read the README file, we won't be able to access the content because it has been tampered with.  
Let's now look at the available versions of the file using:
```bash
git tag
```
Here, we can see a tag named `secret`.  
Let's now look at what is in it using:
```bash
git show secret
```
We can now get the password.  

Once we have it, we can leave the SSH session and move to the next level using the following commands:
```bash
Command: `ssh -p 2220 bandit31@bandit.labs.overthewire.org`
#Password: Retrieved from the `secret` tag
```
<!-- Password: `OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt` -->