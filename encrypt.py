# A Project by David Blunk for the Information Security Administration Class
# Thought coding out the entire problem would better my understanding of this concept
# All code is written by me unless otherwise specified in the comments
# The code is based on https://www.youtube.com/watch?v=9sY57iwNDJw and the Wikipedia article showcasing RSA encryption
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# This function is not my code, couldn't figure out modinverse, so I got some help from Stackoverflow.com
# Modified based on Nikita Tiwari's method.
def inverse(e, phi) : 
    e = e % phi; 
    for x in range(1, phi) : 
        if ((e * x) % phi == 1) : 
            return x 
    return 1

# Taken from daniweb.com since mine was buggy and not optimized
def checkPrime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

# Check for prime and if they are equal, then generate private and public keys
def genkeys(p, q):
    if not (checkPrime(p) and checkPrime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('Both numbers (p and q) cannot be equal')
    n = p * q

    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher
