class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

################## Below CONTEXT code #################

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

################## Below Pseudo code #################
"""

Use the key_to_index method you already created to find which index the tuple should be stored in. When you create the tuple, the key should be in the tuple's index 0 and the value should be in index 1

Where indexes with data will have a tuple, and empty indexes will be filled with None.

Note: the __repr__() method uses the enumerate() function to iterate over the hashmap's key-value pairs.


"""