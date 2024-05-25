Let's delve into the next level challenge.

![untitled](ScreenShots/Level%2027%20->%2028.jpg)

The password for the next level is stored in a Git repository, which we need to access.

---
**What is git?**
- [Git-SCM](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
- [Wikipedia](https://en.wikipedia.org/wiki/Git)
- [Microsoft Learn](https://learn.microsoft.com/en-us/devops/develop/git/what-is-git)
- [Javatpoint](https://www.javatpoint.com/git)
---
Before we clone the repository, we need to create a file in a directory where we have write permissions.  
Since we lack write access in the current directory, we can create a new directory in `/tmp/` and proceed from there:
```bash
mkdir /tmp/bandit27/
cd /tmp/bandit27/
```
Next, let's clone the repository using the following command:
```bash
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
```
Enter the password from the previous level when prompted.  
Once the repository is cloned, you can find the password for the next level.  

After obtaining the password, connect to the next level using SSH with the following commands:
```bash
Command: `ssh -p 2220 bandit28@bandit.labs.overthewire.org`
#Password: Retrieved from the README file
```
<!-- Password: `AVanL161y9rsbcJIsFHuw35rjaOM19nR` -->
