"""
2021-04-29
[leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/)
208. Implement Trie (Prefix Tree)
"""


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


# TrieNode의 word가 필요한 이유
# -> apple이라는 단어를 넣었을때 app이라는 단어가 자동으로 들어간다
# -> word flag로 삽입된 적 있는지 체크!
# Runtime 176 ms (64.70%)
# Memory 31.7 MB (42.62%)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True


if "__main__" == __name__:
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # return True
    print(trie.search("app"))  # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))  # return True
