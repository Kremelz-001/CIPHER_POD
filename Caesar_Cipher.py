from random import randint


def generate_key(n):  # generating a key from a given ordered element space
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = {}
    c = 0
    for k in letters:
        key[k] = letters[(n + c) % len(letters)]
        c += 1
    return key


def encrypt(key, m):  # encode a message with the given key
    m = m.upper()
    cipher = ''
    for c in m:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def key_rev(key):  # To reverse the key dict
    key_update = {}
    for i in key:
        key_update[key[i]] = i
    return key_update


def decrypt(key, enc_message):
    k = key_rev(key)
    end = ''
    for d in enc_message:
        if d in k:
            end += k[d]
        else:
            end += d
    return end


def rand_word(n):  # Generate a random word of a given length
    W = ''
    for i in range(n):
        W += chr(randint(65, 90))
    return W


element = generate_key(randint(1, 9000))
msg = 'STRUCTURES AS ELEMENTS '
enc_msg = encrypt(element, msg)
'''print(msg)

print(enc_msg)
print(decrypt(element,enc_msg))
'''
print(enc_msg)
# Breaking the cipher with the known key
for j in range(26):
    dkey = generate_key(j)
    message = decrypt(dkey, enc_msg)
    print(message)
