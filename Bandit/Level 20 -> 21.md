Let's progress to the next level, transitioning from level 20 to 21.

![untitled](ScreenShots/Level%2020%20->%2021.jpg)

Similar to the previous level, here we encounter a task where we need to input a port number. Upon connection, if the correct password from the preceding level is received, it will provide the password for the subsequent level.

---
**Setting Up a Server Using nc (Netcat)**
-  To establish a server, we'll utilize nc (Netcat), drawing insights from [Varonis](https://www.varonis.com/blog/netcat-commands) and [Computer Hope](https://www.computerhope.com/unix/nc.htm)
---
Based on these references, the server setup involves binding to a specified port and transmitting data when invoked by the ELF file.

Given our constraint of lacking permission to create files directly, we resort to utilizing `echo` for file creation, employing the command:
```bash
echo 'VxCazJaVykI6W36BkBU0mJTCM8rR95XT' | nc -lp {Some_Random_Port_Number} &
```
The `&` suffix enables execution of the server in the background.  
Subsequently, we specify the designated port number to the ELF file:
```bash
./suconnect {Some_Random_Port_Number}
```
Execution of these commands yields the password for the subsequent level.  

Upon obtaining it, we exit the current SSH session and establish a connection to the SSH of the next level using:
```bash
Command: `ssh -p 2220 bandit210@bandit.labs.overthewire.org`
#Password: Retrieved by submitting the password of the previous level
```
<!-- Password: `NvEJF7oVjkddltPSrdKEFOllh9V1IBcq` -->