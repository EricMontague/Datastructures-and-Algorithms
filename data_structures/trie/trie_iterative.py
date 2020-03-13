"""This module contains an implementation of a Trie (Prefix Tree). All
methods are implemented iteratively.
"""


class TrieNode:
    """Class to represent a node in a Trie."""

    def __init__(self):
        self.end_of_word = False
        self.children = {}


class Trie:
    """Class to represent a Trie."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert the given word into the Trie."""
        self._validate_string(word)
        current = self.root
        for character in word:
            #insert character into Trie if not already in it
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character] 
        #at end of word
        current.end_of_word = True

    def starts_with(self, prefix):
        """Return True if there is a word with the given prefix in the Trie,
        otherwise return False.
        """
        self._validate_string(prefix)
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

    def search(self, word):
        """Return True if the given word is in the Trie."""
        self._validate_string(word)
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        #if all characters are in the Trie, but the last character's end_of_word
        #attribute isn't set to True, then the word isn't in the Trie
        return current.end_of_word

    def _validate_string(self, string):
        """Helper method to valid string input for Trie methods."""
        if string == "":
            raise ValueError("Empty strings aren't a valid input.")
        if not isinstance(string, str):
            raise TypeError(f"Expected type of prefix to be 'str', not {type(string)}")

    def count_prefix(self, prefix):
        """Return the number of words in the Trie with the given prefix."""
        self._validate_string(prefix)
        current = self.root
        for character in prefix:
            if character not in current.children:
                return 0
            current = current.children[character]
        return self._dfs(current)

    def _dfs(self, trie_node):
        """DFS Helper method to count the number of words in the Trie with a
        given prefix.
        """
        prefix_count = 0
        stack = [trie_node]
        while stack:
            node = stack.pop()
            if node.end_of_word:
                prefix_count += 1
            for child in node.children.values():
                stack.append(child)
        return prefix_count
    
    def delete(self, word):
        """Delete the given word in the Trie."""
        self._validate_string(word)
        parents = {self.root: None}
        current = self.root
        for character in word:
            if character not in current.children:
                raise ValueError("Word not in Trie.")
            parents[character] = current
            current = current.children[character]
        current.end_of_word = False
        self._delete(parents, word)
            
    def _delete(self, parents, word):
        """Helper method to delete a word from the Trie."""
        for index in range(len(word) - 1, -1, -1):
            character = word[index]
            parent = parents[character]
            if parent.children[character].children:
                break
            parent.children.pop(character)

