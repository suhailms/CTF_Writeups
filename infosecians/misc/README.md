# MISC


## DECODE

```
GAGGCTCTTCTCGCTCGG
```

This is a DNA Sequence.

We can decode the sequence using the below image:

![DNA CODES](/infosecians/img/dna_codes.png)

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

Here is a .pcap file: [inf.pcap](/infosecians/data/inf.pcap)

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

[root.zip](/infosecians/data/root.zip)

Extracted the root.zip
used grep command to search entire subfolders:
```
 grep -r -v "no" *
 
```
flag is: **INF{grep_is_nice}**

--------------------

## key!

