# MISC


## DECODE

```
GAGGCTCTTCTCGCTCGG
```

This is a DNA Sequence.

We can decode the sequence using the below image:

![DNA CODES](img/dna_codes.png)

sauce: https://github.com/JohnHammond/ctf-katana

- GAG - I
- GCT - N
- CTT - F
- CTC - D
- GCT - N
- CGG - A
 
 So the flag is: **INF{INFDNA}**
 
 ------------------------------------

## DUMP

The flag is somewhere in Network Traffic!!

Here is a .pcap file: [inf.pcap](data/inf.pcap)

As all these packets are ICMP and tried to extract the data section.

Well, I solved this in two ways;

using simple strings command:
```
strings analysis.pcap | base64 -d | grep -a flag
```
and using the below script:

```
from scapy.all import *
import base64

capture = rdpcap('inf.pcap')
ping_data = ""

for packet in capture:
   if packet[ICMP].type == 8: # Echo request
       ping_data += packet.load

print base64.b64decode(ping_data)
```
  script credit: BoiteAKlou

Congratulations, ICMP exfiltatration is awesome! The flag is : ndh2k18_017395f4c6312759

we got the flag from the hidden text.

---------------------------------------------------

## GRIP

Can you Search and find the flag inside the ZIP file??

[root.zip](data/root.zip)

Extracted the root.zip
used grep command to search entire subfolders:
```
 grep -r -v "no" *
 
```
flag is: **INF{grep_is_nice}**

--------------------

## key!

John forgot the password to open his sensitive database! can you please help him out??

we have a KeePass2 password database file: [key](data/key)
```
~$ file key
~$ key: Keepass password database 2.x KDBX
```
we need to crack the password for the database.
So first extract the hash from the KeePass database.
We can use KeePass2john tool which is inbuilt in Kali Linux.
```
~$ keepass2john key > keepass.hash
```
No we've the hashfile. To crack the hashfile either we can use hashcat or johntheripper tool.

I'm using hashcat here which will use GPU for faster dictionary attack.
For the wordlist as always ROCKYOU ;)
```
~$ hashcat --force -m 13400 -a 0 -w 1 ./keepass.hash /usr/share/wordlists/rockyou.txt 
hashcat (v5.1.0) starting...

OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-Intel(R) Core(TM) i3-5010U CPU @ 2.10GHz, 2048/5896 MB allocatable, 4MCU
---
--------
$keepass$*2*100000*0*d511838796795889faf887867287640d83e0909dd93632695cf41cac4fd91d62*17b5875b4de1fc45289d81eefa8b7e8c3922b57b26ca6cdc8cdb536a7ad06f51*f9ea64ed89472d4f842562accb754f7d*b8e70313b19c403be159853e51c4336faf291a3aaaf3c85033a1e9374c052b1a*4ca75e72cac19f0dfdc63d9276d1b4442d615772c96c5e91eb9f1e154657730a:police
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: KeePass 1 (AES/Twofish) and KeePass 2 (AES)
Hash.Target......: $keepass$*2*100000*0*d511838796795889faf88786728764...57730a
Time.Started.....: Sun Feb 16 00:00:00 2020 (0 secs)
Time.Estimated...: Sun Feb 16 00:0:00 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
```
once the cracking is finished you'll get the password **police**

Open the database using KeePass(KeePassX in linux) client to open the database and provide the password police.

flag: **INF{kee_pass_file}**

You can also find the cracked password in _.potfile_ which is located in the binary of the hashcat (_~/.hashcat/ or ~/.hashcat/sessions/_) or _--show_ to display the password. If you're using jtr; _john hash --show_

If you want to read more: https://www.rubydevices.com.au/blog/how-to-hack-keepass

-----------------------------------

## FILESYSTEM

Help yourself to put the path to flag.txt together to get the flag for example, if it was located at ab/cd/ef/gh/ij/flag.txt, your flag would be INF{abcdefghij}

we have an [.iso image](data/fsimage.iso.gz)

I'll mount it to go through the files.


-------------------

## INFINITY_ZIPPING

To get the Flag you should follow it to deepest corners of the Universe,you might face some dangers, you gotta go! for you are the chosen one !

File: [infinity_is_cool.zip](data/infinity_is_cool.zip)
