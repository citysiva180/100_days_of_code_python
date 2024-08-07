class HashTable:
    def __init__(self, size=7):

        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def print_table(self):
        for index, val in enumerate(self.data_map):
            print(index, ": ", val)


my_hash_table = HashTable()
my_hash_table.print_table()

# after iterating the string which is in key, we are getting the
# ascii value of that letter and multiplying it by 23. 23 is a prime number. But why 23 right?
# Then we are performing a modulo operation on the my_hash + ordinal value of letter multiplied by 23
# and then getting the reminder which becomes the end length of the code

# At first the data_map attribute will have an empty key value pair of size = 7
