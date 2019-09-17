def decrypt(pk, cipher):
    key, n = pk
    plain = [chr((char ** key) % n) for char in cipher]
    return ''.join(plain)
