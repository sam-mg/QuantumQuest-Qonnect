Let's dive into the next level using the credentials obtained from the previous one.

![untitled](ScreenShots/Level%201%20->%202.jpg)

Upon examining the source code of this level, we notice an intriguing element:
```html
<img src="files/pixel.png">
```
This line of code is particularly suspicious. The presence of a directory path suggests that it resides on the same server hosting this website. By navigating to the directory via the website's URL, we can gain access to its contents.

![untitled](ScreenShots/Level%201%20->%202%20(Files).jpg)

Inside the directory, we find `pixel.png`, which appears to be nothing more than a single white dot. However, the file `users.txt` reveals a list of six users, one of which is associated with natas3.

Armed with the new password found in `users.txt`, we can proceed to the next level using these credentials:
```
URL: http://natas3.natas.labs.overthewire.org
Username: natas3
Password: Password found in the `users.txt`
```
<!-- Password: `G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q` -->