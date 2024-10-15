class Solution:
    def minimumSteps(self, s: str) -> int:
        count_1 = s.count('1')
        temp = len(s)-count_1
        steps = 0
        idx = 0
        idx2 = temp
        while count_1>0:
            while s[idx]!='1':
                idx+=1
            steps += idx2-idx
            idx2+=1
            idx+=1
            count_1-=1
        return steps