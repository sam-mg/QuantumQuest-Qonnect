Let's proceed to the next challenge, moving from level 29 to level 30.

![untitled](ScreenShots/Level%2029%20->%2030.jpg)

To advance, we need to retrieve the password stored in the provided repository.  
This step is slightly more complex than the previous one, but with a systematic approach, it is manageable.

---
**What is `git branch`?**
- Refer to the official [Git-SCM Documentation](https://git-scm.com/docs/git-branch/)
- Additional resources: [W3Schools Git Branch Tutorial](https://www.w3schools.com/git/git_branch.asp?remote=github)

**What is `git checkout`?**
- Refer to the official [Git-SCM Documentation](https://git-scm.com/docs/git-checkout)
- Additional resources: [Atlassain Tutorial](https://www.atlassian.com/git/tutorials/using-branches/git-checkout), [Javatpoint Tutorial](https://www.javatpoint.com/git-checkout)
---
First, we need to create a directory in the `/tmp/` folder and clone the repository using the following commands:
```bash
mkdir /tmp/bandit29/
cd /tmp/bandit29/
git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
```
Although we can read the README file, we won't be able to access the entire content immediately.  
To uncover more details, we'll check the Git logs:
```bash
git log
```
Let's check if there are other users making changes by listing all branches:
```bash
git branch -a
```
We can see that there are four remote branches. Let's switch to the `dev` branch:
```bash
git checkout dev
```
Now, we can view the changes made in the file:
```bash
git show
```
After inspecting the changes, we should be able to retrieve the password.  

Once obtained, we can connect to the next level using the following commands:
```bash
Command: `ssh -p 2220 bandit30@bandit.labs.overthewire.org`
#Password: Retrieved from the README file
```
<!-- Password: `xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS` -->
