class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [n]*(n+1)
        word = set(dictionary)
        dp[0]=0
        for i in range(n):
            dp[i+1]=min(dp[i+1],dp[i]+1)
            for j in range(i+1,n+1):
                if s[i:j] in word:
                    dp[j] = min(dp[j],dp[i])
        return dp[n]