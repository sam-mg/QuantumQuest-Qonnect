# APKrypt

## Description

```
Can you get the ticket without the VIP code?
```

To install the application, follow the instructions provided in the [Anchored Challenge](../Anchored/Anchored.md) for signing and installing the APK.

Once installed, you can inspect the application's source code using `Jadx-GUI`. The flag is revealed in the following code snippet:

```java
if (MainActivity.md5(MainActivity.this.ed1.getText().toString()).equals("735c3628699822c4c1c09219f317a8e9")) {
    Toast.makeText(MainActivity.this.getApplicationContext(), MainActivity.decrypt("k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l"), 1).show();
}
```
To solve this challenge, we can use Frida to hook into the application and calculate the required value. Below is the [Frida script](hook.js) that accomplishes this.

After running the script, input random values into the application's fields. This will reveal the flag:

```
HTB{<some_string>}
```
<!-- HTB{3nj0y_y0ur_v1p_subscr1pt1on} -->