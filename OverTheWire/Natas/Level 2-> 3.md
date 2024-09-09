Let's delve into the next stage by logging in with the credentials obtained from the previous level.

![untitled](ScreenShots/Level%202%20->%203.jpg)

Upon logging in, we encounter a similar scenario as before.  
Following our usual approach, we'll examine the sources tab.

We find this intriguing line in the source code:
```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```
This may not seem like a clue, but a bit of research could lead us in the right direction.

---
**What is robots.txt?**  
According to the official sources [GET /ROBOTS.txt](https://www.robotstxt.org/) and [About /ROBOTS.txt](https://www.robotstxt.org/robotstxt.html) the robots.txt file is a standard used by websites to communicate with web crawlers and other web robots.

---
From these references, we understand that we should inspect the robots.txt file of the website.  
By appending `/robots.txt` to the URL, we can access it.

When we do this, we find the following:
![untitled](ScreenShots/Level%202%20->%203%20(Robots.txt).jpg)

Based on our research, we learn that the Disallow section of robots.txt specifies parts of the website that web crawlers should avoid.

By navigating to the paths listed under the `Disallow` section, we discover the `users.txt` file, which contains the password we need.  

Armed with this password, we can advance to the next level using the following credentials:
```
URL: http://natas4.natas.labs.overthewire.org
Username: natas4
Password: Password found in the `users.txt`
```
<!-- Password: `tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm` -->