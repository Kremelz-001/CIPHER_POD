import math
import random


def isprime(x):
    for n in range(2, math.isqrt(x)):
        if x % n == 0:
            return False

    else:
        return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if isprime(p):
            return p


def is_generator(g, p):
    for k in range(1, p - 1):
        if (g ** k) % p == 1:
            return False
    return True


def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g


p = get_prime(130)
g = get_generator(p)  # corresponding to the prime

print(g, p)
