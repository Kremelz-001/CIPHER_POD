import random
def generate_key_stream(n):
    return bytes([random.randrange(0,256)for i in range(n)])

def xor_bytes (key_stream, message):
    length=min(len(key_stream),len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

m = 'NO ATTACK'
m=m.encode()
key_stream=generate_key_stream(len(m))
cipher=xor_bytes(key_stream,m)


#trying to attack
print(cipher)
message= 'NO ATTACK'
message=message.encode()
guess_key_stream = xor_bytes(cipher)
print(xor_bytes(guess_key_stream,cipher))