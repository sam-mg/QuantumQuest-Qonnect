Let's dive into the next level using the credentials obtained from the previous level.

Upon logging in, we encounter this screen:
![untitled](ScreenShots/Level%205%20->%206.jpg)

---
Examining the source code of this page reveals the following:
```html
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
```
Let's explore what happens when we click the link to view the source code. We see the following:
```php
<?
include "includes/secret.inc";
    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
Next, we need to examine the content of `includes/secret.inc` by appending it to the URL. This allows us to access the secret key, which looks like this:
```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```
With the secret key in hand, we can enter it on the previous page to gain access.

Once we obtain the password, we can progress to the next level using the following credentials:
```
URL: http://natas7.natas.labs.overthewire.org
Username: natas7
Password: Password found by entering the secret key
```
<!-- Password: `jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr` -->