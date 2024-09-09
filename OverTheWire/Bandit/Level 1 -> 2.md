Let's proceed to the next level, which is level 1 to 2.

![untitled](ScreenShots/Level%201%20->%202.jpg)

According to the provided information, the password is stored in a file named with a special character.

---
**How to open a file named with special characters?**
- Refer to [UNIX Power Tools](https://www.cs.ait.ac.th/~on/O/oreilly/unix/upt/ch23_14.htm#:~:text=Sometimes%20you%20can%20slip%20and,with%20a%20dash%20(%20%2D%20)) for insights.
- Find guidance on [Medium](https://medium.com/@.Qubit/how-to-create-open-find-remove-dashed-filename-in-linux-27ee297d1740)
- Utilize search engines for additional assistance.
---
To retrieve the password from the file, execute the following command:   
```bash
cat ./-
``` 
Once you obtain the password, your task within that SSH session is complete. Proceed by disconnecting from the current SSH and connecting to the next level using the following command:
```bash
Command: `ssh -p 2220 bandit2@bandit.labs.overthewire.org`
#The password for the next level is the one obtained from the file named with the special character '-'.
```
<!-- Password: `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi` -->