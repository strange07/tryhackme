# CC: Steganography

[Link to room](https://tryhackme.com/room/ccstego)
Download the zip file

## Steghide

Install steghide by this command

> sudo apt-get install steghide

once you have steghide installed navigate to directory where you downloaded the zip file and unzip it using this command

> unzip spect.zip

1. What argument allows you to embed data(such as files) into other files?

> steghide --help (e????d)

2. What flag let's you set the file to embed?

> steghide --help (-?f)

3. What flag allows you to set the "cover file"?(i.e  the jpg)

> steghide --help 

4. How do you set the password to use for the cover file?

> steghide --help (-?f)

5. What argument allows you to extract data from files?

> steghide --help (e??????t)

6. How do you select the file that you want to extract data from?

> steghide --help (-?f)

7. Given the passphrase "password123", what is the hidden message in the included "jpeg1" file.

> steghide extract -sf jpeg1.jpg

## zsteg

install zsteg by this command

> gem install zsteg

1. How do you specify that the least significant bit comes first

> zsteg --help

2. What about the most significant bit?

> zsteg --help

3. How do you specify verbose mode?

> zsteg --help

4. How do you extract the data from a specific payload?

> zsteg --help

5. In the included file "png1" what is the hidden message?

> zsteg png1.png (n?????????$)

6. What about the payload used to encrypt it.

> zsteg png1.png (?1,b??,??b,?y)

## Exiftools

install exiftools by this command

> sudo apt install exiftool

1. In the included jpeg3 file, what is the document name

> exiftools jpeg3.jpg (????? :))

## Stegoveritas 

install Stegoveritas by these commands

> pip3 install stegoveritas
> stegoveritas_install_deps

1. How do you check the file for metadata?

> stegoveritas --help (-???a)

2. How do you check for steghide hidden information

> stegoveritas --help (-s??????e)

3. What flag allows you to extract LSB data from the image?

> stegoveritas --help (-ex?????????B)

4. In the included image jpeg2 what is the hidden message?

> stegoveritas -steghide jpeg2.jpg (ke????????)

## Spectograms

Install Sonic-Visualizer

1. What is the hidden text in the included wav2 file?

> Open the wav2 file and add spectogram layer 

## The final exam

echo machine-ip >> steganography.com >> /etc/hosts

```nmap
# Nmap 7.80 scan initiated Fri Jun 19 08:06:58 2020 as: nmap -sC -sV -oN nmap.txt stegnography.com
Nmap scan report for stegnography.com (10.10.86.177)
Host is up (0.19s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Test1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jun 19 08:07:13 2020 -- 1 IP address (1 host up) scanned in 14.97 seconds
```

We see a web-server running lets navigate to it

1. What is key 1?

Download the image file(jpeg) from website and check the file by this command

```bash
file exam1.jpeg
```

We will see the password (a???n)

Use steghide to extract data from image using the password 

> s????????y

Submit the key and move to next page and download the wav2 file 

2. What is key 2?

use sonic-visualizer and spectrogram layer and you will get an link like this `https://i???r.com/KTrtNI5` 
move to the link and you will see a image of pencil, download it and use `zsteg` to view the flag

> f???????y

Submit the key and move to next page

3. What is key 3?

we see a qrcode but scanning it does not show any results because of pink layer but stegoveritas has feature of color correction so run this command 

```bash
stegoveritas qrcode.png
```
By scanning one of the image that I get from stegoveritas results I was able to get a link that have flag in it

> k??????t
