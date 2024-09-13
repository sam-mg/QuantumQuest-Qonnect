# HTB Infiltrator: Mobile Challenge - Cat

This write-up covers the most basic mobile challenge in Hack The Box (HTB). Judging by the number of solves, it is evident that this is a very easy challenge.

## Challenge Overview

In this challenge, we are provided with a `.ab` file. These `.ab` files are known as Android Backup Files.

To identify the file type, we can use the following command:
```bash
file <file_name>
```

## Extracting the Backup File

After identifying the file type, we can search online for methods to reverse it. One useful resource is the [Android Backup Extractor on GitHub](https://github.com/nelenkov/android-backup-extractor).

Using this tool, we can extract the contents of the `.ab` file with the following command:
```bash
java -jar abe.jar unpack cat.ab cat.zip
```

Once the extraction is complete, we can unzip the resulting `.zip` file to access its contents.

## Analyzing the Extracted Files

Upon unzipping, we find numerous packages and several SQLite3 databases. After thoroughly examining these files, we initially find nothing of interest.

## The Hidden Clue

However, among the extracted files, we discover six images: five of cute cats and one of a person holding an object. By closely inspecting the object in the person's hand, we uncover the hidden flag.

This challenge demonstrates the importance of attention to detail and thorough analysis in digital forensics.

Happy hacking!