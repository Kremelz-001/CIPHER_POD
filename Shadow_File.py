import hashlib
import base64

def guess_password(salt, iterations, entropy):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1+c2)
            value = base64.b64encode(hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128))
            if value ==entropy:
                return password
    return ''.encode()



iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())
validation = 'SALTED-SHA512-PBKDF2'
entropy = 'kRqabDBsvkyAhpzzVWJtdqbtqgkgNPwr5gqWG6jvw73hxc7CCvC4E33WyR5bxKmAXG5vAG9/ue+DC7BYLHRfOTE/dLKSMdpE9RFH7ZlTp7GHdH5b5vaqQCcKlXAwkky786zvpucDIgGGTOyw6kKB5hqIXLX9chDvcPQksVrjmUs='
password = "??".encode()
password = guess_password(salt,iterations, entropy)
print(password)
value = base64.b64encode(hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128))
print(value)
print(entropy)
'''
print('Alice', validation, iterations, entropy)

password = "password".encode()
salt = 'Hello'.encode()
value = hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)
print('Bob', validation, iterations, entropy)'''
