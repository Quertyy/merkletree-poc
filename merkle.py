from web3 import Web3
import math


class MerkleTree:

    def __init__(self, data_list: list):
        self.data = data_list
        nb_block = len(data_list)
        self.hashes_list = self.__data_hash_list(data_list)
        (total_iteration, start_index) = self.__count_enumeration(nb_block)
        self.iteration_count = total_iteration

    def __data_hash_list(self, data_list: list):
        length = len(data_list)

        hashes_list = [self.__compute_hash(data_list[i]) for i in range(length)]
        return hashes_list

    def __compute_hash(self, hash: str):
        return Web3.keccak(hexstr=hash).hex()

    def __count_enumeration(self, block_count: int):
        total_iteration = math.ceil(math.log2(block_count))
        start_index = block_count - (2**total_iteration)
        return (total_iteration, start_index)

    


    #def __start_iteration(self, start_index: int):
        

    
        


x = MerkleTree(
        [
            "0xAA6cb884573C97E0B26F771ACc0c5C94f6Ae8FFD", 
            "0xCf185Cb08c62Ff969D258FBA18F92dabb278A8A9", 
            "0x0b289dEa4DCb07b8932436C2BA78bA09Fbd34C44", 
            "0xD316F2F1872648a376D8c0937db1b4b10D1Ef8b1", 
            "54655D5468f072D5bcE1577c4a46F701C28a41A7"
        ]
    )

print(x.data)
print(x.hashes_list)
print(x.iteration_count)

