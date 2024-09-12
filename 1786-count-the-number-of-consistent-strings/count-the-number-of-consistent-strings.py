class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars_set = set(allowed)
        count = 0
        for s in words:
            for ch in s:
                if ch not in chars_set:
                    break
            else: 
                count += 1
        return count

        