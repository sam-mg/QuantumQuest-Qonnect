# APKey

## Description

```
This app contains some unique keys. Can you get one?
```

To install, follow the instructions in the [Anchored Challenge](../Anchored/Anchored.md) for signing and installing the application.

Once installed, you can view the source code of the application using `Jadx-GUI`. The flag is displayed in the following code snippet:

```java
if (str.equals("a2a3d412e92d896134d9c9126d756f")) {
    Context applicationContext = MainActivity.this.getApplicationContext();
    MainActivity mainActivity2 = MainActivity.this;
    b bVar2 = mainActivity2.e;
    g gVar = mainActivity2.f;
    makeText = Toast.makeText(applicationContext, b.a(g.a()), 1);
    makeText.show();
}
```

There are several ways to approach this, but let's use Frida to hook and calculate the value. Here is the [script](hook.js) for it.

After executing the script, enter some random values in the fields. You will then obtain the flag:

```
HTB{<some_string>}
```