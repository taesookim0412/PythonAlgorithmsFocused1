class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {'tail': False}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.tree
        for i, char in enumerate(word):
            if char not in curr:
                curr[char] = {'tail': False}
            curr = curr[char]
        curr['tail'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.tree
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return curr['tail']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.tree
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)