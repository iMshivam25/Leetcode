class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for char in str(word):
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_world = True
    def search(self,prefix) -> int:
        curr = self.root
        pref = 0
        for char in str(prefix):
            if char not in curr.children:
                break
            else:
                pref += 1
                curr = curr.children[char]
        return pref

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        max_prefix = 0
        for num2 in arr2:
            max_prefix = max(max_prefix,trie.search(num2))
        return max_prefix