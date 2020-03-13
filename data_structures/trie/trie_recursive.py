"""This module contains an implementation of a Trie (Prefix Tree). All
methods are implemented recursively. The TrieNode class has an extra
attribute, count, that keeps track of the number of words in the trie
that contain that particular character.
"""


class TrieNode:
    """Class to represent a node in a Trie."""

    def __init__(self):
        self.end_of_word = False
        self.count = 0
        self.children = {}


class Trie:
    """Class to represent a Trie."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert the given word into the Trie."""
        self._validate_string(word)
        self._insert(self.root, word, 0)
    
    def _insert(self, current, word, index):
        """Helper method to insert a word into the tree."""
        #Base case: reached end of word
        if index == len(word):
            current.end_of_word = True
        else:
            #if character not a child of current node, 
            #insert it into the Trie
            character = word[index]
            if character not in current.children:
                current.children[character] = TrieNode()
            current.children[character].count += 1    
            self._insert(current.children[character], word, index + 1)

    def starts_with(self, prefix):
        """Return True if there is a word with the given prefix in the Trie,
        otherwise return False.
        """
        self._validate_string(prefix)
        return self._starts_with(self.root, prefix, 0)

    def _starts_with(self, current, prefix, index):
        """Helper method that returns True if there is at least one word in the trie
        with the given prefix.
        """
        #Base case: reached end of prefix
        if index == len(prefix):
            return True
        character = prefix[index]
        if character in current.children:
            return self._starts_with(current.children[character], prefix, index + 1)
        return False

    def search(self, word):
        """Return True if the given word is in the Trie."""
        self._validate_string(word)
        return self._search(self.root, word, 0)
    
    def _search(self, current, word, index):
        """Helper method that returns True if the word is in the trie."""
        #Base case: reached end of prefix
        if index == len(word):
            return current.end_of_word
        character = word[index]
        if character in current.children:
            return self._search(current.children[character], word, index + 1)
        return False

    def _validate_string(self, string):
        """Helper method to valid string input for Trie methods."""
        if string == "":
            raise ValueError("Empty strings aren't a valid input.")
        if not isinstance(string, str):
            raise TypeError(f"Expected type of prefix to be 'str', not {type(string)}")

    def count_prefix(self, prefix):
        """Return the number of words in the Trie with the given prefix."""
        current = self.root
        for character in prefix:
            if character not in current.children:
                return 0
            current = current.children[character]
        return current.count
    
    def delete_word(self, word):
        """Delete the given word in the Trie."""
        self._validate_string(word)
        self._delete(self.root, word, 0)

    def _delete(self, trie_node, word, index):
        """Helper method to delete a word from the Trie."""
        #Recurse until you hit the last character in the word in the trie
        if index == len(word):
            trie_node.end_of_word = False
        else:
            character = word[index]
            to_be_deleted = self._delete(trie_node.children[character], word, index + 1)
            if to_be_deleted:
                #determine how many words in the trie contain this character
                if trie_node.children[character].count <= 1:
                    trie_node.children.pop(character)
                else:
                    trie_node.children[character].count -= 1
        #node shouldn't be deleted if it is the end of a word
        if trie_node.end_of_word:
            return False
        #node shouldn't be deleted if it has children
        if trie_node.children:
            return False
        return True #no children, delete node
        
