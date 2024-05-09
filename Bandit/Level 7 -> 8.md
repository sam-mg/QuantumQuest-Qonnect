Let's delve into the next stage of our challenge, progressing from level 7 to level 8.

![untitled](ScreenShots/Level%207%20->%208.jpg)

In this phase, our objective is to identify the word corresponding to 'millionth'.

---
**Searching for a Specific Word in a File**
- Avail immediate assistance from [Apple Support](https://support.apple.com/en-in/guide/terminal/apd8a205299-1c4c-4845-902a-6190e132b006/mac#:~:text=To%20locate%20a%20string%20within,grep%20prints%20the%20matching%20lines.)
- Explore insights on [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-find-all-files-containing-specific-text-string-on-linux/)
- Seek guidance on [stack overflow](https://stackoverflow.com/questions/16956810/find-all-files-containing-a-specific-text-string-on-linux)
- Harness wisdom from [Red Hat](https://www.redhat.com/sysadmin/find-text-files-using-grep)

---
Employing these resources, we execute the following command:
```bash
cat data.txt | grep "millionth"
```

Upon obtaining the corresponding word, it serves as the flag.  

Subsequently, we exit the current SSH session and transition to the next one using the following directives:
```bash
Command: `ssh -p 2220 bandit8@bandit.labs.overthewire.org`
#Password: Corresponding word to "millionth"
```
<!-- Password: `TESKZC0XvTetK0S9xNwm25STk5iWrBvP` -->