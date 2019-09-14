# A Project by David Blunk for the Information Security Administration Class
# Thought coding out the entire problem would better my understanding of this concept
# All code is written by me unless otherwise specified in the comments
# The code is based on https://www.youtube.com/watch?v=9sY57iwNDJw&t=298s
import math

def main():
    # Since upper and lowercase characters do not matter for RSA, we will put everything to lowercase
    secretCode = input("Enter a secret passphrase: ").lower()
    convertedCode = letterConverter(secretCode)
    p = 0
    q = 0
    # giving p and q values and checking if numbers are prime and actual numbers
    try:
        p = int(input("Enter p: "))
        for iterator in range(2, p):
            if p % iterator is 0:
                exit(0)
        q = int(input("Enter q: "))
        for iterator in range(2, q):
            if q % iterator is 0:
                exit(0)
    except:
        print("p and q have to be prime numbers")
        exit(0)
    phiOfN = (p - 1) * (q - 1)
    print("Pick a number lower than",phiOfN,"for e")
    e = int(input("Enter e: "))
    # Checking for disqualifying factors
    if math.gcd(e,phiOfN) is not 1 or e < 1 or e > phiOfN:
        print("Has to be larger than 1, lower than phi(n), and shares no other factors other than 1")
        exit(0)
    n = p*q
    print("n is",n)

    print("phi(n) is",phiOfN)
    # only thing that I did not write myself
    d = inverse(e,phiOfN)
    print("d is",d)
    print("Cypher # is: ", end="")
    for x in range(0,len(convertedCode)):
        print(pow(int(convertedCode[x]), e) %n , end=" ")


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
            # Putting a value for each character, starting with a being 1
            charValue = ord(charSplit) - 96
            # Adding each value to the phraseNum string
            phraseNum += str(charValue)
        # Putting the values for each part of the passphrase in the convertedCode array
        convertedCode.append(phraseNum)
    return convertedCode


if __name__ == "__main__":
    main()
