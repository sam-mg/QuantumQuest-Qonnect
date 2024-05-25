Let's take this to the next level.

![untitled](ScreenShots/Level%2031%20->%2032.jpg)

To proceed, we need to obtain the password stored in the provided repository.  
While this step is a bit more challenging than the previous one, it remains manageable with a systematic approach.

---
**What is Git `Push`?**
- GitHub's [GitHub](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository) is also a helpful resource.
- Refer to the [Git SCM documentation](https://git-scm.com/docs/git-push).
- For a more tutorial-style explanation, check out [w3schools](https://www.w3schools.com/git/git_push_to_remote.asp?remote=github)

**How to Push Files?**
- Follow the instructions from [Github](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- You might also find this [Datacamp Tutorial](https://www.datacamp.com/tutorial/git-push-pull) useful.
- Another helpful resource is this blog from [InVezza](https://www.invezzatechnologies.com/blog/how-to-push-single-or-two-or-multiple-files-git-single-commit/)
---
First, we need to create a directory in the `/tmp/` folder and clone the repository using the following commands:
```bash
mkdir /tmp/bandit31/
cd /tmp/bandit31/
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
```
After cloning the repository, we'll find a `README` file. When we read it using `cat`, we get the following instructions:
```md
This time your task is to push a file to the remote repository.
Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master
```
Now, let's create the required file and push it. Use the following commands:
```bash
touch key.txt
echo "May I come in?" > key.txt
```
Once the file is created, it's time to push the changes.  
However, this seems too straightforward and might be a bit suspicious.  
Let's inspect the repository contents:
```bash
ls -a
```
We notice a `.gitignore` file. Let's see what's inside by using:
```bash
cat .gitignore
```
The file contains:
```ASCII text
*.txt
```
This means all files ending with .txt are ignored.
To bypass this, we can simply delete the `.gitignore` file:
```bash
rm .gitignore
```
Now, we can proceed to push the file using the following commands:
```bash
git add .
git commit -m "<some_message>"
git push origin master
```
Once this is done, we should have the password. You can now exit and connect to the next level using the following command:
```bash
Command: `ssh -p 2220 bandit32@bandit.labs.overthewire.org`
#Password: Retrieved password after pushing the key
```
<!-- Password: `rmCBvG56y58BXzv98yZGdO7ATVL5dW8y` -->