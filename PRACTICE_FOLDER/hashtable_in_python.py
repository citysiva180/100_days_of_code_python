class HashTable:
    def __init__(self, size=7):
        # At first the data_map attribute will have an empty key value pair of size = 7
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map) # In this expression we understand that we are initializing a hashmap with 7 keys. By which 
            # if we divi

    def print_table(self):
        for index, val in enumerate(self.data_map):
            print(index, ": ", val)


my_hash_table = HashTable()
my_hash_table.print_table()
