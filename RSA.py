from decrypt import *
from encrypt import *

if __name__ == '__main__':
    secretCode = input("Enter a secret passphrase:")
    p = int(input("Enter a prime number: "))
    q = int(input("Enter a different prime number: "))

    print("Generating your public/private keys now . . .")

    public, private = genkeys(p, q)

    print("Public key is ", public)
    print("Private Key key is ", private)

    encryptedMsg = encrypt(private, secretCode)

    print("Cypher # is: ", ''.join(map(lambda x: str(x), encryptedMsg)))
    print("=================================================================")
    print("Decrypting message with public key ", public ," . . .")
    print("Your message is:")
    print(decrypt(public, encryptedMsg))
