class Trie:
    class Node:
        def __init__(self, x):
            self.children = {}
            self.word_end = False
            self.value = x
            return

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = self.Node(c)
                node.children[c] = new_node
                node = new_node
        node.word_end = True
        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.word_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True

t = Trie()
t.insert("abc")
t.search("abc")
t.search("ab")
t.insert("ab")
t.search("ab")
t.insert("ab")
t.search("ab")