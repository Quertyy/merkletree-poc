from Crypto.Hash import keccak

keccak_hash = keccak.new(digest_bits=256)

keccak_hash.update(b'salut')
print(keccak_hash.hexdigest())

class MerkleTree:
    def __init__(self, data_list: list):
        self.data = []
        nb_block = len(data_list)
        self.__add_data(data_list)
        start_index = self.__compute_start_index(nb_block)

    def __add_data(self, data_list: list) -> list:
        for data in data_list:
            self.data.append(data)
        return self.data

    def __compute_start_index(self, data_length: int) -> int:
        count = 0
        while 2**count <= data_length:
            count += 1
        return ((2 ** count) - data_length)

    #def __iteration(self, i: int, start_index: int, total_leaves: int):
        


x = MerkleTree(1)

print(x.data)

