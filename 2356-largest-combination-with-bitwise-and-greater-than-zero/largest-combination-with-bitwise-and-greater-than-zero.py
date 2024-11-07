from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bits = max(candidates).bit_length()  
        max_combination = 0
        for bit in range(max_bits):
            count = 0
            for num in candidates:
                if num & (1 << bit):
                    count += 1
            max_combination = max(max_combination, count)
        
        return max_combination
