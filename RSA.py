import math
import random
from Random_prime_generator import *


def lcm(a, b):
    return a * b // math.gcd(a, b)

def factors(n):
    T = list()
    for x in range(1,n+1):
        if n % x == 0:
            if sorted([x,n//x] not in T):
                T.append((x, n // x))
    return T




def factor(n):
    for p in range(2,n):
        if n%p == 0:
            return p,n//p

def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

#def msgToval(x):            #returns a number for a message


def get_d(e, x):
    for d in range(2, x):
        if d * e % x == 1:
            return d
    return False


# Key generation by Alice
# Step: 1 generate 2 distinct primes

size = 3210
p = get_prime(size)
q = get_prime(size)
print('Generated Primes:', p, q)

# Step 2 compute n=pq

n = p * q
print('Modulus:', n)

# Step 3, Compute Lambda(n)   lcm(a, b) = |ab|/gcd(a, b)
# n = pq, λ(n) = lcm(λ(p), λ(q))
lambda_n = lcm(p - 1, q - 1)

# Step 4 : Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime.

e = get_e(lambda_n)
print('Public Exponent : :', e)

# Step 5 : Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
d = get_d(e, lambda_n)
print('Secret exponent ::', d)

# Key is generated
print('Public Key (e,n):', e, n)
print('Secret Key (d) :', d)

# Bob sending the message
m = 900
print('Actual Message :',m)
c = (m ** e) % n                #Cipher can be made through public key
print('BOB SENDS c:', c)

# Alice decrypting the cipher
m = (c ** d) % n                # Deciphering with the help of private key
print('Alice message received :', m)

#This is Eve

print('\nEve sees: \nPublic Key (e,n):', e,n,'\nEncrypted Message :',c)

p,q = factor(n)
print('Factors:', n)
lambda_n = lcm(p-1,q-1)
print('lambda N:',lambda_n)
d = get_d(e,lambda_n)
print('Secret Exponent by Eve :',e)

m = (c**d) % n
print('Eve message :',m)

print('\nBob not being careful')

msg = 'Nihal'
Ciph= list()
for h in msg:
    c = (ord(h)**e) % n
    Ciph.append(c)
print('Cipher:',Ciph)
M=''
for c in Ciph:
    k = (c**d) % n
    M+=chr(k)
print(M)
