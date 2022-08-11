from Random_prime_generator import *


p = get_prime(100)
h = get_generator(p)
print(p ,h)

#Alice
a = random.randrange(0, p)
g_a = (h**a) % p
# Public
print('Alice g_a:',g_a)

# Bob
b = random.randrange(0,p)
g_b = (h**b) % p
# Public
print('BOB g_b:',g_b)


#Back to alice
g_ab = (g_b**a) % p
print('Alice g_ab:',g_ab)
#BOB'S
g_ba = (g_a**b) % p
print('Bob g_ba:',g_ba)
