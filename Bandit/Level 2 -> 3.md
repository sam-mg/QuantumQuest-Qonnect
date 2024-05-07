Let's delve into the transition from level 2 to level 3.  

![untitled](ScreenShots/Level%202%20->%203.jpg)

In this stage, our task involves handling files with names containing spaces.  

---
**How to Access a File with Spaces in Its Name?**
- For insights, head to [Ask Ubuntu](https://askubuntu.com/questions/516772/how-to-access-files-directories-with-spaces-in-the-name).  
- Check out [MacMost](https://macmost.com/forum/how-do-i-open-a-file-in-terminal-that-has-space-in-its-name.html) for further assistance.  
- Explore [Stack Exchange](https://apple.stackexchange.com/questions/327097/open-a-file-with-spaces-in-the-name-in-terminal) for additional solutions.  

From these references, we identify two primary methods:  
- Utilizing `\ ` (backslash space)  
- Employing quotes such as `'<File_Name>'`  

Allow me to propose a straightforward solution, applicable to any command.  
Imagine a basic command structure: `<Command> <File_Name>`.  
As you input the command and start typing the file name, simply hit the `tab` key on your keyboard after entering the initial characters preceding the spaces.  
This streamlines your workflow significantly.  

---
Now, to acquire the password for the subsequent level, execute either of the following commands:  
```bash
cat spaces\ in\ this\ filename
```  
<p align="center">(or)</p>

```bash
cat 'spaces in this filename' 
```
Both commands achieve the same result.  
Upon obtaining the password, you can proceed to the next level effortlessly.  

Connect to the SSH of the next level with the following command:  
```bash
Command: `ssh -p 2220 bandit3@bandit.labs.overthewire.org`
#Password: Retrieved from the file with spaces in its name
```
<!-- Password: `aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG` -->