# Meow

Welcome to the first step of your journey on [Hack The Box (HTB)](https://app.hackthebox.com/starting-point). Let’s dive right in and get started!

## Setting Up the VPN Connection

Before we can access HTB's machines, we need to set up a VPN connection using `OpenVPN`. Follow the steps below to install and configure it on your system:

First, install OpenVPN using Homebrew:
```bash
brew install openvpn
```
Next, download the `.ovpn` configuration file from the HTB website and connect by running:
```bash
sudo openvpn <file_name>
```
Once connected, you’ll have access to the HTB lab environment and be able to spawn your first machine.

## Answering the Preliminary Questions

Before moving on to the machine, let's answer a few introductory questions:

1. **What does the acronym VM stand for?**  
    - **Answer:** Virtual Machine

2. **What tool do we use to interact with the operating system in order to issue commands via the command line, such as the one to start our VPN connection? It’s also known as a console or shell.**  
    - **Answer:** Terminal

3. **What service do we use to form our VPN connection into HTB labs?**  
    - **Answer:** OpenVPN

4. **What tool do we use to test our connection to the target with an ICMP echo request?**  
    - **Answer:** Ping

5. **What is the name of the most common tool for finding open ports on a target?**  
    - **Answer:** Nmap

6. **What service do we identify on port 23/tcp during our scans?**  
    - **Answer:** Telnet

7. **What username is able to log into the target over telnet with a blank password?**  
    - **Answer:** Root

## Interacting with the Machine

With the initial setup done, let’s move on to the machine. To access it, we’ll use the `Telnet` service discovered on port `23/tcp`.

Connect to the machine using:
```bash
telnet <IP_Address>
```
The following output will appear:
```
Trying <IP_Address>...
Connected to <IP_Address>.
Escape character is '^]'.

  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█

Meow login:
```
The username for login is `root`. Once logged in, we can explore the system.

To list all files in the current directory, use the following command:
```bash
ls
```
Among the files, you will see `flag.txt`. To view the contents of this file, run:
```bash
cat flag.txt
```
Upon retrieving the flag, submit it to complete the box.  Congratulations, you've completed the ***Meow*** challenge!