class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

################## Below CONTEXT code #################

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


################## Below Pseudo code #################
"""

exists takes a word as input, and should return True if the word exists in the trie, and False if it doesn't.

    Loop over each nested dictionary in the trie associated with the letters in the word.
    If you get to a character that doesn't exist in the trie, return False.
    Once you get to the last letter, return True if end_symbol is in its dictionary, and False if it isn't.

"""