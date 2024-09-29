class AllOne:

    def __init__(self):
        self.dic = defaultdict(int)

    def inc(self, key: str) -> None:
        self.dic[key] += 1  # Increment the whole key

    def dec(self, key: str) -> None:
        if key in self.dic:
            self.dic[key] -= 1  # Decrement the whole key
            if self.dic[key] == 0:
                del self.dic[key]  # Remove the key if its count goes to zero

    def getMaxKey(self) -> str:
        if not self.dic:
            return ""
        max_key = max(self.dic, key=self.dic.get)  # Get the key with the maximum value
        return max_key

    def getMinKey(self) -> str:
        if not self.dic:
            return ""
        min_key = min(self.dic, key=self.dic.get)  # Get the key with the minimum value
        return min_key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
