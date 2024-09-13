class Trie:
    def find_matches(self, document):
        matches = set()
        doc_length = len(document)
        
        for start_index in range(doc_length):
            current = self.root
            for end_index in range(start_index, doc_length):
                char = document[end_index]
                if char not in current:
                    break
                current = current[char]
                if self.end_symbol in current:
                    matches.add(document[start_index:end_index + 1])
        
        return matches

################## Below CONTEXT code #################

  def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True


################## Below Pseudo code #################
"""

find_matches takes an entire document string as input and should return a set() of all the words from the trie that occur in the document.

    Create a new set() to store the matches.
    Loop over all the indexes of the characters in the document
        Create a temporary level variable to hold the current level (a dictionary), and initialize it to the root of the trie.
        Use a nested loop to iterate over all the indexes of characters in the document, but start at the current index of the outer loop.
            If the inner character is not in the level dictionary break out of the inner loop.
            Otherwise, set level to the dictionary for the current inner character.
            If the inner character's level contains the end symbol, add the word to the matches set. You can calculate the word by slicing the document using the indexes of the outer and inner loops.
    Return the matches set.

"""