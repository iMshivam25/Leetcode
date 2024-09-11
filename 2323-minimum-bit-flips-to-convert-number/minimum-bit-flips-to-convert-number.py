class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        exor_dec = start ^ goal
        exor_bin = bin(exor_dec)[2:]
        return str(exor_bin).count('1')