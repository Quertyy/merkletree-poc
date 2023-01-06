from Crypto.Hash import keccak
import sha3

def hash(x):
    hash = x
    ## keccak256 de hash
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(hash.encode('utf-8'))
    return keccak_hash.hexdigest()  

print(hash("AA6cb884573C97E0B26F771ACc0c5C94f6Ae8FFD"))

