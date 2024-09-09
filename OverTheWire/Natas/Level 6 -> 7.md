Let's now log into the next level using the credentials from the previous level.

Upon logging in, we are greeted with the following interface:
![untitled](ScreenShots/Level%206%20->%207.jpg)

---
Let's examine these two buttons closely; they must serve some purpose. By inspecting the source code of the webpage, we find two crucial clues:
```html
<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```
These two buttons represent a vulnerability in this level. We can exploit them to retrieve the password for the next level. When either button is pressed, the URL changes accordingly, for example:
```
http://natas7.natas.labs.overthewire.org/index.php?page=home
```
Let's modify this URL to suit our needs. By altering the URL, specifically by removing `home` at the end, we get:
![untitled](ScreenShots/Level%206%20->%207%20(Index.php).jpg)
In the `index.php` file, it is apparent that files located in the `page` are being opened. We can manipulate this to access the file containing the next level's password. The modified URL should be:
```
http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8
```
This URL indicates that we are navigating up four directories to reach the desired file. Upon executing this, we obtain the password for the next level.

Armed with the new password, we can log into the next level with the following credentials:
```
URL: http://natas8.natas.labs.overthewire.org
Username: natas8
Password: Password obtained from natas_webpass
```
<!-- Password: `a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB` -->