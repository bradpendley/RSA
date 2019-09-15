# A Project by David Blunk for the Information Security Administration Class
# Thought coding out the entire problem would better my understanding of this concept
# All code is written by me unless otherwise specified in the comments
# The code is based on https://www.youtube.com/watch?v=9sY57iwNDJw and the Wikipedia article showcasing RSA encryption
import math

def main():
    # Since upper and lowercase characters do not matter for RSA, we will put everything to lowercase
    secretCode = input("Enter a secret passphrase: ").lower()
    convertedCode = letterConverter(secretCode)
    # giving p and q values and checking if numbers are prime and actual numbers
    p = pickP()
    q = pickQ()
    phiOfN = (p - 1) * (q - 1)
    print("Pick a number lower than",phiOfN,"for e")
    e = pickE(phiOfN)
    n = p*q
    print("\n\n\n----------------")
    print("n is",n)
    print("phi(n) is",phiOfN)
    d = inverse(e,phiOfN)
    print("Public key is e:",e,"n:",n)
    print("Private Key key is d:",d,"n:",n)
    print("Cypher # is \"", end="")
    for x in range(0,len(convertedCode)):
        # breaking this up to make it read a bit easier
        powerOf = pow(int(convertedCode[x]),e)
        moduleOf = powerOf % n
        print(moduleOf, end=" ")
    print("\b\"\n----------------")

def pickE(phiOfN):
    e = ""
    try:
        e = int(input("Enter e: "))
    except:
        print("e has to be an integer")
        pickE(phiOfN)
    # Checking for disqualifying factors
    if math.gcd(e,phiOfN) is not 1 or e < 1 or e > phiOfN:
        print("Has to be larger than 1, lower than phi(n), and shares no other factors other than 1")
        pickE(phiOfN)
    return e

def pickP():
    p = ""
    try:
        p = int(input("Enter p: "))
        isPrime = checkPrime(p)
        if isPrime is not True:
            print("q has to be a prime number")
            pickQ()
        return p
    except:
        print("Please enter an integer")
        pickP()


def pickQ():
    q = ""
    try:
        q = int(input("Enter q: "))
        isPrime = checkPrime(q)
        if isPrime is not True:
            print("q has to be a prime number")
            pickQ()
        return q
    except:
        print("Please enter an integer")
        pickQ()


# Taken from daniweb.com since mine was buggy and not optimized
def checkPrime(num):
    if num < 2:
        return False
    if num is 2:
        return True
    if not num & 1:
        return False
    for x in range(3, int(num ** 0.5) + 1, 2):
        if num % x == 0:
            return False
    return True



# This function is not my code, couldn't figure out modinverse, so I got some help from Stackoverflow.com
def inverse(e, phi):
    a, b, u = 0, phi, 1
    while(e > 0):
        q = b // e
        e, a, b, u = b % e, u, e, a-q*u
    if (b == 1):
        return a % phi
    else:
        print("Must be coprime!")
        exit(0)


def letterConverter(secretCode):
    # Splitting by space
    codesplit = secretCode.split()
    # Declaring an empty array for the converted code to be filled in later
    convertedCode = []
    # A loop for each index of the secretcode
    for arraySplit in codesplit:
        # Declaring a variable to fill in the converted code after the loop
        phraseNum = ""
        # Splitting up the index by characters
        for charSplit in arraySplit:
            # Putting a value for each character, starting with a being 1 (using ASCII tables, so will be buggy with anything else but regular characters)
            charValue = ord(charSplit) - 96
            # Adding each value to the phraseNum string
            phraseNum += str(charValue)
        # Putting the values for each part of the passphrase in the convertedCode array
        convertedCode.append(phraseNum)
    return convertedCode


if __name__ == "__main__":
    main()
