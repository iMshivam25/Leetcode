class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        score = 0
        while k>0:
            max_ele = -heapq.heappop(nums)
            score += max_ele
            heapq.heappush(nums, -(math.ceil(max_ele/3)))
            k-=1
        return score