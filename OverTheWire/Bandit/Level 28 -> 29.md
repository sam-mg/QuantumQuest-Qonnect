Lets now look into the next level.

![untitled](ScreenShots/Level%2028%20->%2029.jpg)

To move forward, we'll need to retrieve the password stored in the repository provided.  
This step is slightly more complex than the previous level, but manageable with a systematic approach.

---
First, we need to create a directory in the `/tmp/` folder and clone the repository using the following commands:
```bash
mkdir /tmp/bandit28/
cd /tmp/bandit28/
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
```
Although we can read the README file, we won't be able to access the entire content immediately.  
To uncover more details, we'll check the Git logs:
```bash
git log
```
By inspecting the logs, we can identify changes in the data.  
To examine these changes, we'll use the `git show` command:
```bash
git show
```
After obtaining the password from the changes in the repository, we can exit the current SSH session and connect to the next level with the following command:
```bash
Command: `ssh -p 2220 bandit29@bandit.labs.overthewire.org`
#Password: Retrieved from the README file
```
<!-- Password: `tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S` -->