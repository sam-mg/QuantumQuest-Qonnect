# Pinned

## Description

```
This app has stored my credentials and I can only login automatically. I tried to intercept the login request and restore my password, but this seems to be a secure connection. Can you help bypass this security restriction and intercept the password in plaintext?
```

To install the application, follow the instructions in the [Anchored Challenge](../Anchored/Anchored.md) for signing and installing the APK.

Once installed, we can examine the source code. Modify the password to `1234567890987654`. After this, capture the traffic using [HTTP Toolkit](https://httptoolkit.com). However, you might encounter the following error:
```
Certificate rejected for connection to pinned.com
```

To resolve this, we need the application to accept our certificate by bypassing SSL Pinning. Use Frida for this:
```bash
frida -U -f com.example.pinned -l ssl_pinning_universal_bypass_with_CA.js
```
Once bypassed, monitor the traffic using [HTTP Toolkit](https://httptoolkit.com). When a request is made from the app, you will see the following message in the request:
```
uname=bnavarro&pass=HTB{<some_string>}
```

Here is the flag:
```
HTB{<some_string>}
```
