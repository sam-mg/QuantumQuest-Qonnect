To move forward, we need to log into the next level using the credentials obtained from the previous level.

Upon logging in, we are greeted with the following screen:
![untitled](ScreenShots/Level%203%20->%204.jpg)

---
**What is `Referer` according to HTTP headers?**  
The `Referer` HTTP header indicates the address of the previous web page from which a link to the currently requested page was followed.  

This can be verified from several sources:
- Referring from [mdn web docs_](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer#)
- Also from [Geeksforgeeks](https://www.geeksforgeeks.org/http-headers-referer/)
- Getting information from [Wikipedia](https://en.wikipedia.org/wiki/HTTP_referer)
---
Examining the code behind the reload button, we find the following HTML snippet:
```html
<div id="viewsource"><a href="index.php">Refresh page</a></div>
```

Upon clicking this button, the following transition happens:
![untitled](ScreenShots/Level%203%20->%204%20(Index.php).jpg)
as well as this change in the URL:
```php
http://natas4.natas.labs.overthewire.org/index.php
```

We then delve into the network activity for deeper insights.
![untitled](ScreenShots/Level%203%20->%204%20(Network).jpg)

Here, we can see that the referer is from natas4, but according to the description, it should be from natas5. Let's try changing it.
There are two ways to do that:
1. Using Python:
    ```py
    import requests
    url = "http://natas4.natas.labs.overthewire.org/"
    user = "natas4"
    password = "REDACTED"
    referer = "http://natas5.natas.labs.overthewire.org/"

    r = requests.get(url, auth=(user, password), headers={'referer': referer})
    print(r.text)
    ```
2. Burp Suite:
    <!-- 
    We can modify the request using Burp Suite. This is my first time using Burp Suite, so let's walk through the process:
    - Target Tab: Open the browser from the Target tab.
    - Input URL: Enter the URL to monitor traffic in Burp.
    - Login: Use the provided credentials to log in.
    - Proxy Tab: Navigate to the Proxy tab to see the network requests.
    -->
    Let's change the `Referer` from `natas4` to `natas5` and observe the outcome.  
    ![untitled](ScreenShots/Level%203%20->%204%20(Burp%20Suite).jpg)
    
After making this change, we receive the password for the next level.

With this, we can log into the next level using the following credentials:
```
URL: http://natas5.natas.labs.overthewire.org
Username: natas5
Password: Password found by changing the referer
```
<!-- Password: `Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD` -->