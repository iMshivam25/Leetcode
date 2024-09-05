class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        sum_n = mean * (n + len(rolls)) - sum_m
        limit = 6*n
        if isinstance(sum_n, float) or sum_n > limit or sum_n < n:
            ans = []
            return ans
        else:
            ans = [1]*n
            sum_n -= n
            idx = 0
            while(sum_n != 0):
                ans[idx]+=1
                if ans[idx]==6:
                    idx+=1
                sum_n-=1
            return ans
            

