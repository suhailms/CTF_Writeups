#!/usr/bin/env python3

import sys

def enc_image(a):
    f1 = open(a,'rb')
    data1 = bytearray(f1.read())
    size = len(data1)
    enc = bytearray(size)
    tmp = 0
    enc[0] = data1[0]
    for i in range(1,size):
        enc[i] = data1[i-1] ^ data1[i]
    f1.close()
    with open('encrypted','wb') as f:
        f.write(enc)


print('='*25+"Menu"+'='*25)
print('Press 1 for encryption\n')
print('Press 2 for dencryption\n')
image_name = input('Enter the path to the file ')
password = input('Enter the password to be encrypted with ')
a = enc_image(image_name)
print('The encrypted file is saved as encrypted')
