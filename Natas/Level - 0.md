Let's delve into the Level 0 challenge of Natas.

![untitled](ScreenShots/Level%20-%200.jpg)

The Natas challenges are designed to help individuals gain a solid understanding of server-side web security.

---
Let's explore the zeroth level. Upon accessing the website, we are prompted to enter login details.
![untitled](ScreenShots/Level%20-%200%20(Login%20Page).jpg)
For the initial level, the credentials are:
```
URL: http://natas0.natas.labs.overthewire.org
Username: natas0
Password: natas0
```
For the initial level, the credentials are:
![untitled](ScreenShots/Level%20-%200%20(Initial%20Page).jpg)

Now, let's inspect the website to see what information it contains. You can inspect the webpage using the following methods:
1. Right-click anywhere on the webpage and select `inspect`
1. Use the shortcut `Cmd + Opt + C` on Mac
2. Use the shortcut `Ctrl + Shift + C` on Linux
3. Press `F12` on Windows
By using these key combinations, you can inspect the elements of the website. When we examine the source code, we find the following:
```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script>
<script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas0", "pass": "natas0" };</script>
</head>
<body>
<h1>natas0</h1>
<div id="content">
You can find the password for the next level on this page.
<!--The password for natas1 is RETRACTED -->
</div>
</body>
</html>
```

From this code, we can deduce that the password for the next level is hidden in the HTML comments.

Let's now log into the next level using the following credentials:
```
URL: http://natas1.natas.labs.overthewire.org
Username: natas1
Password: Password found in the source code
```
<!-- Passowrd: g9D9cREhslqBKtcA2uocGHPfMZVzeFK6 -->