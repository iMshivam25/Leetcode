class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        arr = []
        skill = sorted(skill)
        for idx in range(len(skill)//2):
            temp = []
            temp.append(skill[idx])
            temp.append(skill[len(skill)-1-idx])
            arr.append(temp)
        product = 0
        prev_sum = arr[0][0]+arr[0][1]
        for row in arr:
            if prev_sum != row[0]+row[1]:
                return -1
            prev_sum = row[0]+row[1]
            product += row[0]*row[1]
        return product