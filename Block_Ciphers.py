#Double DES

from pyDes import *
import random


message='Hello There'
key_11 = random.randrange(0,256)
key_1 = bytes([key_11,0,0,0,0,0,0,0])
key_21 = random.randrange(0,256)
key_2 = bytes([key_21,0,0,0,0,0,0,0])
iv = bytes([random.randrange(0,256)]*8)
k1=des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2=des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

#Alce Sending Encrypted messages
cipher = k1.encrypt(k2.encrypt(message))
print('Key 11 :',key_11)
print('Key 21:', key_21)
print('Encrypted:',cipher)

#Bob
message = k2.decrypt(k1.decrypt(cipher))
print('Decrypted:', message)

def modify(cipher):
    mod=[0]*len(cipher)
    mod[8]= 1
    return bytes([mod[i]^cipher[i] for i in range(len(cipher))])


#Eves's Attack
lookup = dict()
for i in range(256):
    key= bytes([i,0,0,0,0,0,0,0])
    k = des(key,ECB,iv,pad=None,padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i
print(lookup)
for j in range(256):
    key = bytes([j,0,0,0,0,0,0,0])
    k = des(key,ECB,iv, pad=None,padmode=PAD_PKCS5) #encrypting message using key-1 = decrypting the cipher using key_2


    if k.decrypt(cipher) in lookup:
        print('key21::',lookup[k.decrypt(cipher)])
        print('key11::',j)
        key_1=bytes([j,0,0,0,0,0,0,0])
        key_2 = bytes([lookup[k.decrypt(cipher)],0,0,0,0,0,0,0])
        k1 = des(key_1,ECB,iv,pad=None,padmode=PAD_PKCS5)
        k2= des(key_2,ECB,iv,pad=None,padmode=PAD_PKCS5)
        print('EVE HERE double des broken:',k2.decrypt(k1.decrypt(cipher)))
        break
