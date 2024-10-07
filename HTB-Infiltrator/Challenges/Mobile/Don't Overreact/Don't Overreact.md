# Don't Overreact

## Description

```
Some web developers wrote this fancy new app! It's really cool, isn't it?
```

Let's first open the application in [JADX](https://github.com/skylot/jadx). After opening it, we can see that there is only one activity, and it doesn't contain much information.

Remember, the description mentions that this app is built by web developers. This suggests that it is a React Native application.

To reverse engineer React Native applications, I found a useful guide [here](https://securityqueens.co.uk/android-attack-reversing-react-native-applications/). Let's follow these steps:

1. Debug the application using `Apktool`:
    ```bash
    apktool d <file_name>
    ```
2. Navigate to the assets directory:
    ```bash
    cd assets/
    ```
3. In the assets directory, you'll find a file named `index.android.bundle`. This is the crucial file we need to work on.

When we open this file, it appears to be minified and difficult to read. We can use [Unminify](https://unminify.com) to beautify the data. Once formatted, the content becomes readable.

After examining the file, we find a Base64 encoded string at the end:
```
SFRCezxzb21lX3N0cmluZz59
```

Decoding this string reveals the flag:
```
HTB{<some_string>}
```