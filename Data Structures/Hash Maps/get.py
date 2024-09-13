class HashMap:
    def get(self, key):
        index = self.key_to_index(key)
        bucket = self.hashmap[index]
        if bucket is None:
            raise Exception("sorry, key not found")
        return bucket[1]

################## Below CONTEXT code #################

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

################## Below Pseudo code #################
"""

the get method. It takes a key (a string) and returns the value stored at that location (not the whole key/value tuple).

Use the key_to_index method to find the correct index to lookup in the self.hashmap datastore, and if a value doesn't exist at that index, raise the following Exception to indicate no key was found.

raise Exception("sorry, key not found")

Note: Due to our toy implementation, some of the keys that are inserted into the hashmap have colliding values, which may lead to unexpected results.


"""