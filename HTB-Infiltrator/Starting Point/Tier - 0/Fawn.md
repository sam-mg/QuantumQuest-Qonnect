# Fawn - The Next Challenge in HTB

Continuing on our Hack The Box (HTB) journey, the next challenge is **Fawn**. Similar to our previous task, we'll first need to connect to the HTB VPN. For setup instructions, you can refer to [Meow](Meow.md). Once connected, you'll have access to the lab environment and be able to spawn your machine.

## Answering the Preliminary Questions

Before jumping into the machine interaction, let's answer some basic questions to reinforce our knowledge:

1. **What does the 3-letter acronym FTP stand for?**  
    - **Answer:** File Transfer Protocol

2. **Which port does the FTP service listen on usually?**  
    - **Answer:** 21

3. **FTP sends data in the clear, without any encryption. What acronym is used for a later protocol designed to provide similar functionality to FTP but securely, as an extension of the SSH protocol?**  
    - **Answer:** SFTP

4. **What is the command we can use to send an ICMP echo request to test our connection to the target?**  
    - **Answer:** Ping

5. **From your scans, what version is FTP running on the target?**  
    - **Answer:** After running the following command:
        ```bash
        nmap -sV <IP_Address>
        ```
        We see that the result shows `vsftpd 3.0.3`.

6. **From your scans, what OS type is running on the target?**  
    - **Answer:** Unix

7. **What is the command we need to run in order to display the 'ftp' client help menu?**  
    - **Answer:** `ftp -h`

8. **What is the username that is used over FTP when you want to log in without having an account?**  
    - **Answer:** Anonymous

9. **What is the response code we get for the FTP message 'Login successful'?**  
    - **Answer:** 230

10. **There are a couple of commands we can use to list the files and directories available on the FTP server. One is `dir`. What is the other command that is a common way to list files on a Linux system?**  
    - **Answer:** `ls`

11. **What is the command used to download the file we found on the FTP server?**  
    - **Answer:** `get`

---

## Interacting with the Machine

Now, let's interact with the machine. We can connect to it using the following command:
```bash
ftp <IP_Address>
```

You should see output similar to the following:
```
Connected to 10.129.30.213.
220 (vsFTPd 3.0.3)
Name (10.129.30.213:<user_name>): Anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```
In the questionnaire, we identified that the username is `Anonymous`. Enter this when prompted for a username. For the password, you can input anything, as FTP allows anonymous login without a password.

Once logged in, list the files available on the server using:
```bash
ls
```
The output should be something like this:
```
229 Entering Extended Passive Mode (|||64448|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp>
```
We can see that there's a file called `flag.txt`. To download this file, use the `get` command as follows:
```bash
get flag.txt
```
Upon downloading the file, retrieve the flag, submit it, and complete the box! Congratulations, you've successfully completed the ***Fawn*** challenge!