class Trie:
    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        return self.search_level(current, prefix, words)

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for letter in sorted(cur.keys()):
            if letter != self.end_symbol:
                self.search_level(cur[letter], cur_prefix + letter, words)
        return words

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

words_with_prefix takes a prefix as input, and returns a list of all the words in the trie that start with that prefix.

    Create an empty list to hold the words.
    Traverse the trie, down to the level of the last character in the prefix. If the prefix is not in the trie, return an empty list.
    Starting at the level of the last character in the prefix, call search_level with the current level, the prefix, and the list of words.
    Return the words you get back from search_level.

search_level takes the current level (cur), the prefix, and the current word list as inputs. It returns all the words found in the current level and below, plus whatever words were passed in.

    If self.end_symbol is in the current level, add the current prefix to the list of words.
    Use the .keys() dictionary method to get the keys in the current level.
    Iterate over each key in the current level, and be sure to use the sorted() to iterate in a deterministic order.
        If the key is not self.end_symbol, then recursively call search_level on the next level. Be sure to update the cur_prefix to include the key you just traversed.
        The words list is updated by the recursive call.
    Return the words.


"""