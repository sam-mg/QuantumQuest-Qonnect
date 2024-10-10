# Manager

## Description

```
A client asked me to perform security assessment on this password management application. Can you help me?
```

Let's start an instance in HTB and note the `IP` and `Port`. Initially, we are prompted to enter user details and a password. We can either try common credentials or register as a new user.

Upon capturing the traffic, we observe a POST request being sent. After logging in, we can edit the password and view our role and ID.

Interestingly, the ID is `1`, indicating no previous users. What if we could change the admin's password and gain access? By editing our password, we can modify the request to change the username to `admin` and set a new password for the `admin` account.

The edited request:
```
username=admin&password=password
```

The response will look like this:
```
{"id":1,"username":"admin","password":"password","role":"HTB{<some_string>}"}
```

And here we get our flag.
<!-- HTB{b4d_p@ss_m4n@g3m3nT_@pp} -->