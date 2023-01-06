from Crypto.Hash import keccak
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
        keccak_hash = keccak.new(digest_bits=256)
        keccak_hash.update(hash.encode('utf-8'))
        return keccak_hash.hexdigest()

    def __count_enumeration(self, block_count: int):
        total_iteration = math.ceil(math.log2(block_count))
        start_index = block_count - (2**total_iteration)
        return (total_iteration, start_index)

    


    #def __start_iteration(self, start_index: int):
        

    
        


x = MerkleTree(["salut", "sa", "va", "oui", "et"])

print(x.data)
print(x.hashes_list)
print(x.iteration_count)

