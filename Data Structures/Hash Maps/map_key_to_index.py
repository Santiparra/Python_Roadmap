class HashMap:
    def key_to_index(self, key):
        total = 0
        for char in key:
            total += ord(char)
        index = total % len(self.hashmap)   
        return index

################## Below CONTEXT code #################

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

################## Below Pseudo code #################
"""

    Take a key (string) as input
    Add the Unicode values of all the characters in the string using Python's ord function
    Mod ( % ) the sum by the size of the hashmap to get an index which should be an int
    Return the index


"""