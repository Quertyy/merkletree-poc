from web3 import Web3
import math


class MerkleTree:
    '''
    This is a simple implementation of the merkle tree structure
    It uses the keccak256 hashing algorithm on hexadecimal strings
    Args:
        data_list (list): Array of data that you want to hash
        sorted_pairs (bool): If set to true, the hashing pairs will be sorted
    '''
    def __init__(self, data_list: list, sorted_pairs=False):
        self.data = data_list
        self.hashes_list = []
        self.leaves = self.__data_hash_list(self.data)
        nb_block = len(data_list)
        (total_iteration, start_index) = self.__count_enumeration(nb_block)
        self.hashes_list.append(self.__data_hash_list(self.data))
        self.hashes_list = self.__create_merkle_tree(
            total_iteration,
            self.hashes_list,
            sorted_pairs
        )
    
    def __create_merkle_tree(self, total_iteration, data: list, sorted_pairs: bool):
        for i in range(total_iteration):
            current_list = data[i]
            list_to_hash = []
            for x, y in zip(current_list[::2], current_list[1::2]):
                if sorted_pairs:
                    sorted_list = sorted([x,y])
                    x, y = sorted_list[0], sorted_list[1][2:]
                else :
                    y = y[2:]
                list_to_hash.append(x + y)
            
            hash_list = self.__data_hash_list(list_to_hash)
            if len(current_list) % 2 == 1:
                hash_list.append(current_list[-1])
            self.hashes_list.append(hash_list)
        return self.hashes_list

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

    def get_total_hash_levels(self):
        return self.iteration_count - 1
    
    def get_layers(self):
        return self.hashes_list

    def get_leaves(self):
        return self.leaves

    def get_root(self):
        return "".join(self.hashes_list[-1])