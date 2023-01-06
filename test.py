from web3 import Web3

def hash(x):
    return Web3.keccak(hexstr=x).hex()

print(hash("0xAA6cb884573C97E0B26F771ACc0c5C94f6Ae8FFD"))

