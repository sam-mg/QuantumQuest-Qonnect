To move forward, we need to log into the next level using the credentials obtained from the previous level.

Upon logging in, we are greeted with the following screen:
![untitled](ScreenShots/Level%203%20->%204.jpg)

---
**What is `Referer` according to HTTP headers?**
- Referring from [mdn web docs_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer#)
- Also from [Geeksforgeeks](https://www.geeksforgeeks.org/http-headers-referer/)
- Getting information from [Wikipedia](https://en.wikipedia.org/wiki/HTTP_referer)
---
Examining the code behind the reload button, we find:
```html
<div id="viewsource"><a href="index.php">Refresh page</a></div>
```

Upon clicking this button, the following transition happens:
![untitled](ScreenShots/Level%203%20->%204%20(Index.php).jpg)

Upon clicking this button, the URL transforms into:
```php
http://natas4.natas.labs.overthewire.org/index.php
```

We then delve into the network activity for deeper insights.
![untitled](ScreenShots/Level%203%20->%204%20(Network).jpg)
<!-- 
We can modify the request using Burp Suite. This is my first time using Burp Suite, so let's walk through the process:
- Target Tab: Open the browser from the Target tab.
- Input URL: Enter the URL to monitor traffic in Burp.
- Login: Use the provided credentials to log in.
- Proxy Tab: Navigate to the Proxy tab to see the network requests.
-->
Let's change the `Referer` from `natas4` to `natas5` and observe the outcome.  
After making this change, we receive the password for the next level.
![untitled](ScreenShots/Level%203%20->%204%20(Burp%20Suite).jpg)
In the Proxy tab, we notice that the `Referer` is set to `natas4`.  
However, it needs to be `natas5` as per the challenge description.  
Lets change it and look at what happens.  
We now get the password for the next level. 

With this, we can log into the next level using the following credentials:
```
URL: http://natas5.natas.labs.overthewire.org
Username: natas5
Password: Password found by changing the referer
```
<!-- Password: `Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD` -->