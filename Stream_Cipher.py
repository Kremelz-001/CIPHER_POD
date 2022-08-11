import pygame

import random


class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(cipher, x):
    b = []
    for i in cipher:
        if random.randrange(0, x) == 0:
            i = i ^ 2 ** random.randrange(0, 8)
        b.append(i)
    return bytes(b)


def modification(cipher):  # intervening in the cipher sent to the bank by alice
    mod = [0] * len(cipher)
    mod[9] = ord(' ') ^ ord('1')
    mod[10] = ord(' ') ^ ord('0')
    mod[11] = ord('1') ^ ord('0')
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))


def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])


def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[o] ^ cipher[o] for o in range(length)])


def brute_force(plain, cipher):
    for k in range(2 ** 31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
    return False


secret_key = random.randrange(0,2**6)
key = KeyStream(secret_key)
header = 'MESSAGE:'
message = header + 'This sentence is False.'
message = message.encode()
print('FROM EVE')
print(message)
cipher = encrypt(key, message)

# Bob
key = KeyStream(secret_key)
message = encrypt(key, cipher)
print('BOB HERE')
print(message)

# Eve Brute Force breakage
bf_key = brute_force(header.encode(), cipher)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print('EVE HERE, HA HA')
print('I found your key:',bf_key)
print(message)