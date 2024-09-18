class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1,len(nums)):
                if int(str(nums[idx1])+str(nums[idx2]))<=int(str(nums[idx2])+str(nums[idx1])):
                    temp = nums[idx1]
                    nums[idx1] = nums[idx2]
                    nums[idx2] = temp
        ans = ""
        for num in nums:
            ans+=str(num)
        if nums[0]==0:
            return '0'
        return ans