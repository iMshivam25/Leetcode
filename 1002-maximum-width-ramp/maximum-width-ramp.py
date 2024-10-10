class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # First pass: Build a decreasing stack
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        maxr = 0
        # Second pass: Check for possible ramps
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                maxr = max(maxr, j - stack.pop())
        
        return maxr
