# Biohazard

[link to room](https://tryhackme.com/room/biohazard)

echo machine-ip biohazard >> /etc/hosts

## Introduction

```nmap
# Nmap 7.80 scan initiated Wed Jun 17 09:50:01 2020 as: nmap -sC -sV -oN nmap.txt biohazard.com
Nmap scan report for biohazard.com (10.10.158.94)
Host is up (0.20s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c9:03:aa:aa:ea:a9:f1:f4:09:79:c0:47:41:16:f1:9b (RSA)
|   256 2e:1d:83:11:65:03:b4:78:e9:6d:94:d1:3b:db:f4:d6 (ECDSA)
|_  256 91:3d:e4:4f:ab:aa:e2:9e:44:af:d3:57:86:70:bc:39 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Beginning of the end
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 17 09:50:38 2020 -- 1 IP address (1 host up) scanned in 36.53 seconds
```

1. How many open ports?

> check nmap results

2. What is the team name in operation

> visit the website (????? AL??? team)

## The Mansion

###### Flag Hunting

visit the website and go the embedded link i.e http://biohazard.com/mansionmain/ 
check the website source code and move to next web-page i.e http://biohazard.com/?????/

> go to embedded link and you will get the `emblem flag`

check the website again and you will get a base64 encoded string

```bash
!-- SG93IGFib3V0IHRoZSAvdGVhUm9vbS8=
echo !-- SG93IGFib3V0IHRoZSAvdGVhUm9vbS8= | base64 -d
```

goto the webpage http://biohazard.com/base64_decoded/
go to embedded link and you will get the `lock pick flag`

go to the page mentioned in webiste i.e http://biohazard.com/artRoom/ and go to embedded link 

`we will get a map of website `

visit the http://biohazard.com/barRoom/ and enter the lock pick flag

you will get a base32 encoded string decode it and you will get `music note flag`

enter the `music note flag` in the bar room and we will get redirected to `secret bar room`

enter the `emblem flag` and this will give us a name 

```
re????a
```

visit http://biohazard.com/diningRoom/ again put the `gold emblem flag` and you will get a viginere cipher and the key is the name we got from secret bar room i.e `re????a` 
`klfvg ks r wimgnd biz mpuiui ulg fiemok tqod. Xii jvmc tbkg ks tempgf tyi_hvgct_jljinf_kvc`
after decoding it visit the page http://biohazard.com/diningRoom/viginere_cipher/ we well get the `shield flag`

visit http://biohazard.com/diningRoom2F/ and check the source code you will get a rot13 encrypted string

after that visit the page http://biohazard.com/diningRoom/rot13_decrypted/ 
you will get the `blue gem flag`

###### Crest Hunting

visit http://biohazard.com/tigerStatusRoom/ and enter the `blue jewel flag`
```
crest 1:
S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9
Hint 1: Crest 1 has been encoded twice
Hint 2: Crest 1 contanis 14 letters

S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9 (base64)
KJWFEUKJJBLHUWSYJE3ESRY= (base32)
RlRQIHVzZXI6IG (final)

```
visit http://biohazard.com/galleryRoom/ and the goto the embedded link named as EXAMINES
```
crest 2:
GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE
Hint 1: Crest 2 has been encoded twice
Hint 2: Crest 2 contanis 18 letters

GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE (base32)
5KeuGWm3LHY85cckxhB3gAQMD (base58)
h1bnRlciwgRlRQIHBh (final)
```

visit http://biohazard.com/armorRoom/  and enter the shield flag

```
crest 3:
MDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMDAgMDExMDAxMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDA= (base64 > binary)
Hint 1: Crest 3 has been encoded three times
Hint 2: Crest 3 contanis 19 letters

63 33 4d 36 49 48 6c 76 64 56 39 6a 59 57 35 30 58 32 68 (HEX)
c3M6IHlvdV9jYW50X2h (final)
```

visit http://biohazard.com/attic/ and enter the shield key

```
crest 4:
gSUERauVpvKzRpyPpuYz66JDmRTbJubaoArM6CAQsnVwte6zF9J4GGYyun3k5qM9ma4s (base58)
Hint 1: Crest 2 has been encoded twice
Hint 2: Crest 2 contanis 17 characters

70 5a 47 56 66 5a 6d 39 79 5a 58 5a 6c 63 67 3d 3d (HEX)
pZGVfZm9yZXZlcg== (final)
```
```
CREST 1 + CREST 2 + CREST 3 + CREST 4 = 
RlRQIHVzZXI6IGh1bnRlciwgRlRQIHBhc3M6IHlvdV9jYW50X2hpZGVfZm9yZXZlcg== (base64)
```
> FTP user: ??????, FTP pass: ?????????????

## The Guard House

Login into ftp and download all the files

###### Finding keys


1. Key 1 

> use steghide to extract key

2. Key 2

> use exiftool to view the key

3. Key 3 

> Use binwalk to extract the key

```
Password for the encrypted file
	Final key: Key 1 + Key 2 + Key 3
	cGxhbnQ0Ml9jYW5fYmVfZGVzdHJveV93aXRoX3Zqb2x0 (base64)
```

use gpg to decrypt the file and get `helmet_flag`

## The Revisit

1. SSH Username

visit http://biohazard.com/studyRoom/ and enter the helmet flag to downlad a doom.tar.gz file 
extract it by running this command

> tar -xzvf doom.tar.gz

2. SSH Password

> visit http://biohazard.com/hidden_closet/ and read the wold_medal.txt

3. STARS bravo Team leader

> visit http://biohazard.com/hidden_closet/ to find the answer

## Underground Labouratory

1. Where you found chris 

> check hidden files

2. Who is the traitor? 

> read chris.txt

3. Login Password for weasker?

> visit http://biohazard.com/hidden_closet/ and copy the hash(viginere) using the key you found in chris.txt

4. The name of the ultimate form

> read weasker_note.txt

5. root flag

> weasker have the permission to read the flag so we donot need any escalation
