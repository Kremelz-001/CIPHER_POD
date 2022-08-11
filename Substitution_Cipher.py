from random import randint

def generate_key():
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key=dict()
    cletters=list(letters)
    for c in letters:
        key[c]=cletters.pop(randint(0,len(cletters)-1))
    return key

def encrypt(key,message):
    end=''
    for i in message:
        if i in key:
            end += key[i]
        else:
            end+= i
    return end

def get_dkey(key):
    r_key={}
    for i in key:
        r_key[key[i]]=i
    return r_key







key=generate_key()
print(key)
msg='HI THERE'
print(msg)
cipher=encrypt(key,msg)
print(cipher)
print(encrypt(get_dkey(key),cipher))



