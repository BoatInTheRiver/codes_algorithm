#coding:utf-8

'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
'''

class Trie:
    def __init__(self):
        self.lookup = {}

    def insert(self, word):
        tree = self.lookup
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['#'] = '#'

    def search(self, word):
        tree = self.lookup
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if '#' in tree:
            return True
        return False

    def startsWith(self, prefix):
        tree = self.lookup
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
