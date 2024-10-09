# Anchored

## Description

```
A client asked me to check if I can intercept the https request and get the value of the secret parameter that is passed along with the user's email. The application is intended to run in a non-rooted device. Can you help me find a way to intercept this value in plain text.
```

When I tried installing the app, I encountered the following error:
```
adb: failed to install Files/Anchored.apk: Failure [-124: Failed parse during installPackageLI: Targeting R+ (version 30 and above) requires the resources.arsc of installed APKs to be stored uncompressed and aligned on a 4-byte boundary]
```

To resolve this, I used `apktool` to debug and rebuild the application:
```bash
apktool d Anchored.apk
apktool b Anchored/
```

Next, we need to sign the application. Here are the commands to sign your application:
```bash
zipalign -v 4 Anchored/dist/Anchored.apk Anchored/dist/Anchored-aligned.apk
apksigner sign --ks your-keystore.jks --out Anchored/dist/Anchored-signed.apk Anchored/dist/Anchored-aligned.apk
apksigner verify Anchored/dist/Anchored-signed.apk
```

After signing, you can install the application using:
```bash
adb install Anchored/dist/Anchored-signed.apk
```

To capture the traffic, we can use [HTTP Toolkit](https://httptoolkit.com). However, when attempting this, we encounter the following error:
```
Certificate rejected for connection to anchored.com
```

To resolve this, we need the application to accept our certificate. This involves bypassing SSL Pinning. We can achieve this using Frida for both `root bypass` and `SSL pinning bypass`:
```bash
frida -U -f com.example.anchored -l root_bypass.js -l ssl_pinning_universal_bypass_with_CA.js
```

Once done, we can monitor the traffic using [HTTP Toolkit](https://httptoolkit.com). When a request is made from the app, we get the following message added to the request:
```
msg=<some_string>&mail=try%40gmail.com&
```

Let's format it as a flag:
```
HTB{<some_string>}
```