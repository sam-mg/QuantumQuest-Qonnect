# Dancing - The Next Challenge in HTB

Continuing our Hack The Box (HTB) journey, the next challenge is **Dancing**. Like before, we need to connect to the HTB VPN. If you need a refresher on how to set this up, refer to [Meow](Meow.md). Once connected, you’ll gain access to the lab environment and can spawn your machine.

## Answering the Preliminary Questions

Before we interact with the machine, let’s go through some questions to solidify our understanding:

1. **What does the 3-letter acronym SMB stand for?**  
    - **Answer:** Server Message Block

2. **What port does SMB use to operate at?**  
    - **Answer:** 445

3. **What is the service name for port 445 that came up in our Nmap scan?**  
    - **Answer:** Microsoft-DS

4. **What is the 'flag' or 'switch' that we can use with the `smbclient` utility to 'list' the available shares on Dancing?**  
    - **Answer:** `-L`

5. **How many shares are there on Dancing?**  
    - **Answer:** 4

6. **What is the name of the share we are able to access in the end with a blank password?**  
    - **Answer:** WorkShares

7. **What is the command we can use within the SMB shell to download the files we find?**  
    - **Answer:** `get`

## Interacting with the Machine

Now, let's connect to the SMB service on the machine. We’ll use the following command to access the `WorkShares` share:
```bash
smbclient \\\\<IP_Address>\\WorkShares
```
You’ll be prompted for a password:
```
Password for [WORKGROUP\<user_name>]:
```
Since no password is required, you can simply press Enter.

Once inside the SMB shell, you’ll see the following prompt:
```bash
Try "help" to get a list of possible commands.
smb: \>
```
To list the available directories and files, use the `ls` command. You should see two directories. Navigate into these directories and use the get command to download the files.

In one of the files, you’ll find the flag. Use the command below to download it:
```bash
get <file_name>
```
After downloading and retrieving the flag, submit it to complete the box. Congratulations, you've successfully completed the ***Dancing*** challenge!