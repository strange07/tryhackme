# Easy Steganography

[Link to room](https://tryhackme.com/room/easysteganography)

Download the zip file and extract it, we will get four similar images

#### 1. Flag 1

```
by using steghide and binwalk i cannot find anything
lets check hex-dump but because we don't know the flag format so I'll have to try different combinations 
````
``` bash
hexdump -C flag1.jpeg | grep S
```

> Ste?????

#### 2. Flag 2

```
using binwalk to extract images from then opening them, i was able to find the flag 
```
```bash
binwalk --dd '.*' flag2.jpeg
```

> AL???????

#### 3. Flag 3

```
I was able to get the flag by just using strings
```

```bash
strings flag3.jpeg
```

> M??h

#### 4. Flag 4

```
this image has also xml embedded in it 
lets use binwalk to extract the xml file
```

```bash
binwalk --dd '.*' flag4.jpeg
```

reading the xml file i was able to get the flag

> Try????????
