# Angler

## Description

```
The skilled fisherman used his full strength and expertise to hook the fish. Can you beat him and set the fish free?
```

We can view the source code of the application using `Jadx-GUI`. When we look into the `MainActivity.java`, we can see this
```java
if (intent.getStringExtra("Is_on").equals("yes")) {
    Toast.makeText(context, "Look me inside", 1).show();
    printStream = System.out;
    str = MainActivity.this.getInfo(C0813d.m2714d("XDR"));
} else {
    printStream = System.out;
    str = "I am Strong, no one can defeat me";
}
```

Here, we find that `XDR` is sent to `m2714d`. Upon examining `m2714d`, we see:

```java
public static String m2714d(String str) {
    char[] charArray = str.toCharArray();
    for (int i3 = 0; i3 < charArray.length; i3++) {
        charArray[i3] = (char) (charArray[i3] ^ 16);
    }
    return String.valueOf(charArray);
}
```

When we input `XDR` into this function, we get `HTB` using [Cyberchef](https://cyberchef.io/#recipe=XOR(%7B'option':'Decimal','string':'16'%7D,'Standard',false)&input=SFRC). This value is then sent to a native function:

```java
static {
    System.loadLibrary("angler");
}
public native String getInfo(String str);
```

Next, we decompile the code using IDA. It appears to return a string. We attempt to read it using this [Frida script](Hook%20Return%20Value.js), but nothing is printed. Remembering the BroadcastReceiver, we set it using the adb command:

```shell
adb shell am broadcast -a android.intent.action.BATTERY_LOW --es Is_on yes
```

After setting this, we see the result in the Frida script:

```
getInfo result: I am not here, I am there
```

We delve deeper into the native function. In IDA, we find `Java_com_example_angler_MainActivity_getInfo`, which contains:

```c
illusion(v3);
ne(&v6);
```

Examining the `ne` function, we see:

```c++
if ( !strcmp(a2, v23) )
    std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::basic_string<decltype(nullptr)>( a1, "You found the flag");
else
    std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::basic_string<decltype(nullptr)>(a1, "I am not here, I am there");
```

We can hook the native function to monitor string comparisons using this [Frida script](Hook%20String%20Comparisons%20(Without%20Checking).js). Numerous strings are printed. Recall that we obtained `HTB` by XORing with `16`. We check if this is used in comparisons with the updated [Frida Script](Hook%20String%20Comparisons%20(With%20Checking).js).

We get the output:

```
strcmp called with arguments: 'HTB' and '4854427b3c736f6d655f737472696e673e7d'
```

What is the second string? Using [dCode](https://www.dcode.fr/cipher-identifier), we identify it as ASCII code. Decoding it on [ASCII Code](https://www.dcode.fr/ascii-code), we retrieve the flag:

```
HTB{<some_string>}
```