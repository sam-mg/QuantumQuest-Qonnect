Let's now delve into the next level by using the credentials obtained from the previous stage.

![untitled](ScreenShots/Level%2010%20->%2011.jpg)

Upon examining the source code, we find the following PHP script:
```php
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';
    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}
function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}
function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
$data = loadData($defaultdata);
if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}
saveData($data);
?>
```

Let's break down what is happening in this code. The script uses a XOR encryption function to encode and decode data, which is then stored in a cookie. The `loadData` function reads the cookie, decrypts the data using XOR, and checks for the `showpassword` and bgcolor values. If these values are present and valid, it updates the `$mydata` array. Finally, the `saveData` function encrypts the `$data` array and sets it as a cookie.

To move forward, we need to find the encryption key used in the XOR function. Once we have the key, we can encode the string `{"showpassword":"yes","bgcolor":"#000000"}` and store it in the cookie. This will grant us access to the next level.

Here's a Python script to determine the key and encode the required data:
```py
import base64
import json
from urllib.parse import unquote

def xor_string(string, key):
    repeated_key = (key * (len(string) // len(key))) + key[:len(string) % len(key)]
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(string, repeated_key))
    return result

def b64_decode(string):
    return base64.b64decode(string).decode()

def b64_encode(string):
    return base64.b64encode(string.encode()).decode()

preset_cookie = "MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="
preset_string = {"showpassword":"no","bgcolor":"#000000"}
required_string = {"showpassword":"yes","bgcolor":"#000000"}

# Making a string which is just base64 Encrypted
key_base64 = b64_encode((json.dumps(preset_string)))
key = b64_decode(key_base64)

# Getting the key using the cookie ^ simple key
decoded_cookie = b64_decode(unquote(preset_cookie))
new_key = xor_string(decoded_cookie, key)[:4]

# XOR the required string with key
required_xor = xor_string((json.dumps(required_string)), new_key)
required_b64 = b64_encode(required_xor)
print(required_b64)
```
Running this script will give us the new encoded value to set in the cookie. After setting this cookie, we can reload the page to retrieve the password for the next level.

With the obtained password, we can advance to the next level using the following credentials:
```
URL: http://natas12.natas.labs.overthewire.org
Username: natas12
Password: Password obtained via changing cookie value
```
<!-- YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG -->