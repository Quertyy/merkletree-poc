from web3 import Web3
import math


class MerkleTree:

    def __init__(self, data_list: list):
        self.data = data_list
        self.hashes_list = []
        nb_block = len(data_list)
        (total_iteration, start_index) = self.__count_enumeration(nb_block)
        self.iteration_count = total_iteration
        self.hashes_list.append(self.__data_hash_list(self.data))
        
        for i in range(total_iteration):
            current_list = self.hashes_list[i]
            list_to_hash = []
            for x, y in zip(current_list[::2], current_list[1::2]):
                y = y[2:]
                print(f'concat {x + y}')
                list_to_hash.append(x + y)
            
            hash_list = self.__data_hash_list(list_to_hash)
            if len(current_list) % 2 == 1:
                hash_list.append(current_list[-1])
            self.hashes_list.append(hash_list)
            

        

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

    def get_total_iteration(self):
        return self.iteration_count
    
    def get_layers(self):
        return self.hashes_list

    
        

    
        


x = MerkleTree(
        [
            "0xAA6cb884573C97E0B26F771ACc0c5C94f6Ae8FFD", 
            "0xCf185Cb08c62Ff969D258FBA18F92dabb278A8A9", 
            "0x0b289dEa4DCb07b8932436C2BA78bA09Fbd34C44", 
            "0xD316F2F1872648a376D8c0937db1b4b10D1Ef8b1", 
            "0x54655D5468f072D5bcE1577c4a46F701C28a41A7",
            "0x9a90b4ca0c5d986A6370c5C0d7985500F47C00fB",
            "0x241055aEF1180dAFF2F8D71B5F51f77bbC564998",
            "0xC35cAC128302CB860Ef2D3634a17025AF7a671F7",
            "0xd1E1F5Ea4D14CbD0044F90938648eCE9d84C7Ca1",
            "0x7eF61cAcD0C785eAcDFe17649d1c5BcBA676a858",
            "0xf7FdEEED754b2E5fd9d826bfDf18844ee7E2D303"
        ]
    )





print(x.get_layers())
print(x.get_total_iteration())