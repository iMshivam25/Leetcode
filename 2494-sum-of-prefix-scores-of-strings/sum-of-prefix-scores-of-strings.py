class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr = curr.children[char]
            curr.count+=1
    def score(self,word)->int:
        curr = self.root
        total = 0
        for char in word:
            total+=curr.children[char].count
            curr = curr.children[char]
        return total
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.score(word))
        return ans

        