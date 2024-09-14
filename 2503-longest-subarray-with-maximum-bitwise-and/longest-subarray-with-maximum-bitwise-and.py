class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_count = 0
        count = 0
        for num in nums:
            if num == max_val:
                count += 1
                max_count = max(count,max_count)
            else:
                count=0
        return max_count