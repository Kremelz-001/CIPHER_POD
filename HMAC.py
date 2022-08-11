import hashlib
import base64

def modify(m):
    l=list(m)
    l[0] = l[0]^1
    return bytes(l)
# alice and bob share a secret key

secret_key = 'secretKey'.encode()

# alice wants to make a MAC
m = 'Hey, Bob. How are you ?'.encode()
x = hashlib.sha256()
x.update(secret_key)
x.update(m)
HMAC = base64.b64encode(x.digest())                  # only defined via the message and secret key

print(m, HMAC)


# Eve comes along
m = modify(m)
print(m)

# Bob Receives and validates HMAC

j = hashlib.sha256()
j.update(secret_key)
j.update(m)
Hmac = base64.b64encode(j.digest())
print(Hmac)

