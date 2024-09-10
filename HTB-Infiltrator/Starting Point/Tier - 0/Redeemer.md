# Redeemer - The Next Challenge in HTB

Continuing our Hack The Box (HTB) journey, the next challenge is **Redeemer**. Like before, we need to connect to the HTB VPN. If you need instructions on how to set this up, refer to [Meow](Meow.md). Once connected, you'll gain access to the lab environment and be able to spawn your machine.

## Answering the Preliminary Questions

Before interacting with the machine, let’s go through some questions to solidify our understanding:

1. **Which TCP port is open on the machine?**  
    - **Answer:** We can find that using:
        ```bash
        nmap -p- -Pn --min-rate 5000 -sV <IP_Address>
        ```
        The result shows that port `6379` is open.

2. **Which service is running on the port that is open on the machine?**  
    - **Answer:** Redis

3. **What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database**  
    - **Answer:** In-Memory Database

4. **Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.**  
    - **Answer:** `redis-cli`

5. **Which flag is used with the Redis command-line utility to specify the hostname?**  
    - **Answer:** `-h`

6. **Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?**  
    - **Answer:** `info`

7. **What is the version of the Redis server being used on the target machine?**  
    - **Answer:** You can find this by using:
        ```bash
        redis-cli -h <IP_Address>
        ```
        The result will show the version, which is `5.0.7`.

8. **Which command is used to select the desired database in Redis?**  
    - **Answer:** `select`

9. **How many keys are present inside the database with index 0?**  
    - **Answer:** 4

10. **Which command is used to obtain all the keys in a database?**  
    - **Answer:** `keys *`

## Interacting with the Machine

To interact with the Redis service on the machine, you can connect using:
```bash
redis-cli -h <IP_Address>
```
Once connected, you can use the command `keys *` to list all the keys available in the database. To retrieve the content of any key, use the `get` command:
```bash
get <key_name>
```
After retrieving the flag, submit it to complete the box. Congratulations, you've successfully completed the ***Redeemer*** challenge!