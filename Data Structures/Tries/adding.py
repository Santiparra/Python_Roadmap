class Trie:
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True

################## Below CONTEXT code #################

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

################## Below Pseudo code #################
"""

add takes a word as input, and should add it to the trie.

    Assign a temporary variable current to the root dictionary of the trie.
    Loop over each character in the word.
        If the character is not a key in the current dictionary, add it and assign a new empty dictionary to it.
        Update the current dictionary to point to the child dictionary corresponding to the character in the loop.
    Once you've ensured all the dictionaries exist, add the self.end_symbol to the dictionary of the last character in the word. This will indicate that this is a complete word and not just a prefix of another word.


"""