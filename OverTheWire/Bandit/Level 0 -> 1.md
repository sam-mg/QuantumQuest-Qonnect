Let's now proceed to the next level, Level 0 -> 1:

![untitled](ScreenShots/Level%200%20->%201.jpg)

The task at this level involves retrieving the password from a file located in the home directory.  

---
**How to list files?**
- Utilize the `ls` (list) command to list all files in the current directory.  

**How to inspect the contents of a file?**
- Implement the `cat` command to examine the contents of a file.
---
You can obtain the password from the file using the following command:   
```bash
cat readme
```  
Once you've accessed the file and retrieved the necessary information, you can terminate the SSH connection.  
Then, proceed to the subsequent level using the following command:  
```bash
Command: `ssh -p 2220 bandit1@bandit.labs.overthewire.org`
#The password for the next level is the one obtained from the 'readme' file.
```
<!-- Password: `NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL` -->