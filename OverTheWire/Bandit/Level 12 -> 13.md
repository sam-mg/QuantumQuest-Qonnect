Let's delve into levels 12 to 13, my personal favorite challenge!

![untitled](ScreenShots/Level%2012%20->%2013.jpg)

Our objective here is to reverse a file that has been repeatedly compressed by creating a copy of the `data.txt` file in the `tmp` folder.

---
**How to identify file types?**
- I drew insights from [TECHMINT](https://www.tecmint.com/find-file-types-in-linux/), [phoenixNAP](https://phoenixnap.com/kb/linux-file-command), [GeeksforGeeks](https://phoenixnap.com/kb/linux-file-command), and [Javatpoint](https://www.javatpoint.com/linux-file) to master this.

**How to reverse a hex dump file?**
- I referenced [tutorialspoint](https://www.tutorialspoint.com/unix_commands/xxd.htm) and [Die](https://linux.die.net/man/1/xxd) for this technique.

**How to reverse a gzip file?**
- Valuable guidance came from [Linuxize](https://linuxize.com/post/gzip-command-in-linux/) and the generous community at [Stack Exchange](https://unix.stackexchange.com/questions/301964/how-can-i-undo-an-incorrect-gzip)

**How to reverse a bzip2 file?**
- I explored strategies from [TECHMINT](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/) and sought advice from seasoned users on [Super User](https://superuser.com/questions/480950/how-to-decompress-a-bz2-file)

**How to reverse a tar file?**
- My journey through this involved learning from the expertise shared by [nixCraft](https://www.cyberciti.biz/faq/howto-extract-tar-file-to-specific-directory-on-unixlinux/) and [How-To Geek](https://www.howtogeek.com/248780/how-to-compress-and-extract-files-using-the-tar-command-on-linux/)

With these invaluable references, we're equipped to tackle this challenge effectively.

---
Now, let's explore the commands for reversing:
1. Hex Dump
    ```bash
    xxd -r {input_file} > {output_file}  
    ```
2. gzip files
    ```bash
    gzip -d < {input_file} > {output_file}
    ```
3. bzip2 files
    ```bash
    bzip2 -d < {input_file} > {output_file}
    ```
4. tar files
    ```bash
    tar xf {input_file} -O > {output_file} 
    ```

We'll need to execute these commands in sequence to unlock the password.  
Follow these steps diligently:
```bash
mkdir /tmp/bandit12/
cp data.txt /tmp/bandit12/
cd /tmp/bandit12/
xxd -r data.txt > file1
gzip -d < file1 > file2
bzip2 -d < file2 > file3
gzip -d < file3 > file4
tar xf file4 -O > file5
tar xf file5 -O > file6
bzip2 -d < file6 > file7
tar xf file7 -O file8
gzip -d < file8 > file9
cat file9
```

Executing these commands flawlessly will reveal the password for the next level.  

Once you have it, exit the current SSH session and connect to the next one using:
```bash
Command: `ssh -p 2220 bandit13@bandit.labs.overthewire.org`
#Password: The text from the final file
```
<!-- Password: `wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw` -->