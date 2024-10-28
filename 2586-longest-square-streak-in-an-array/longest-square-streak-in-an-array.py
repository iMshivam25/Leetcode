class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)  # Use a set for fast lookup
        max_streak = 0

        for num in nums:
            current = num
            streak = 1
            while current * current in nums_set:
                current = current * current
                streak += 1
            max_streak = max(max_streak, streak)
        
        return max_streak if max_streak > 1 else -1