class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        sum_n = mean * (n + len(rolls)) - sum_m
        limit = 6*n
        if isinstance(sum_n, float) or sum_n > limit or sum_n < n:
            ans = []
            return ans
        else:
            ans = [sum_n//n]*n
            remainder = sum_n%n
            for i in range(remainder):
                ans[i]+=1
            return ans
            

