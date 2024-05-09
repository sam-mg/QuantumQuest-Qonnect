Let's elevate our challenge from Level 8 to Level 9!

![untitled](ScreenShots/Level%208%20->%209.jpg)

Our mission at this juncture is to identify the elusive word that appears only once amidst a sea of repetitions.

---
**Methods for Tallying Word Frequencies:**
- Drawing insights from [SuperUser](https://superuser.com/questions/59833/how-to-count-the-number-of-occurrences-of-each-word-in-a-file)
- Seeking wisdom from [stack exchange](https://unix.stackexchange.com/questions/39039/get-text-file-word-occurrence-count-of-all-words-print-output-sorted)
- Alternatively, crafting a Python script with guidance from [GeekforGeeks](https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file/)

---
Let's embark on this challenge with two distinct strategies:
1. Pythonic Prowess:
    ```python
    text = open("data.txt", "r") 
    d = dict() 
    for line in text: 
        lines = line.strip().split(" ")
        for word in lines:
            if word in d: 
                d[word] = d[word] + 1
            else: 
                d[word] = 1
    for key in list(d.keys()): 
        if d[key] == 1:
            print(key, ":", d[key])
    ```
2. Command-Line Crusade:
    ```bash
    cat data.txt | tr -s ' ' '\n' | sort | uniq -u
    ```
    <p align="center">(or)</p>

    ```bash
    cat data.txt | tr -s ' ' '\n' | sort | uniq -u | sort -nr
    ```
    <p align="center">(or)</p> 

    ```bash
    sort data.txt | uniq -u | sort -r
    ```
    These commands, though similar, draw inspiration from diverse sources.

Once we unveil the solitary word, it becomes the key to unlocking the door to the next level:

```bash
Command: `ssh -p 2220 bandit9@bandit.labs.overthewire.org`
#Password: [The Singular Word]
```
<!-- Password: `en632plfyizbn3phvk3xogslninne00t` -->
