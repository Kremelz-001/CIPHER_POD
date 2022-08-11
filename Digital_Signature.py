import hashlib

# These are Alice's RSA keys
# Public Key (e,n): 5 19596671
# Secret Key (d) : 3917549

def modify(x):
    l= list(x)
    l[0] = l[0]^1
    return bytes(l)

n = 19596671
e = 5
d = 3917549

# Message that Alice wants to sign and send to Bob
msg = 'Hello, Bob'.encode()

# Step 1 hash the msg
x = hashlib.sha256()
x.update(msg)
y = x.digest()  # hash value
y = int.from_bytes(y, 'big') % n            #int hash
print('Hash Value :', y)

# Decrypt the Hash value using secret exponent

sign = (y ** d) % n
# Evil Eve
msg = modify(msg)







# send msg with sign to bob

print(msg, sign)

# Bob Verifying the sign
# get the hash value of the msg
x = hashlib.sha256()
x.update(msg)
y = x.digest()  # hash value
y = int.from_bytes(y, 'big') % n
print('Hash Value :', y)

# step 2 verify the sign

verification = (sign ** e) % n
print('Verification :', verification)
