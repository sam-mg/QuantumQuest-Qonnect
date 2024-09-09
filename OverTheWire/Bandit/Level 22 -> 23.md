Let's delve into the forthcoming challenge, transitioning from level 22 to 23.

![untitled](ScreenShots/Level%2022%20->%2023.jpg)

Upon initial examination, it appears that this level follows a similar pattern to its predecessor.  
However, there's a twist: new commands await execution.

---
Now, echoing our previous approach, we navigate to the designated directory:
```bash
cd /etc/cron.d/
ls
```
As before, our target is `cronjob_bandit23`. Let's inspect its contents:
```bash
cat cronjob_bandit23
```
This yields the following output:
```bash
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```
Following suit, we proceed to scrutinize the `cronjob_bandit23.sh` script:
```sh
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
This script computes an MD5 hash of the user's name and employs it to save the password file.  
To replicate this process in our terminal, we execute:
```bash
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
```
Resulting in the output:
```bash
8ca319486bfbbc3663ea0fbe81326349
```
Now, let's retrieve the password stored in `/tmp/`:
```bash
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```
Upon acquiring the password, we're poised to ascend to the next level.  

To proceed, we utilize SSH:
```bash
Command: `ssh -p 2220 bandit23@bandit.labs.overthewire.org`
#Password: Use the retrieved password from the `/tmp/` directory.
```
<!-- Password: `QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G` -->