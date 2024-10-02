class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        ranked_map = {val:rank+1 for rank,val in enumerate(sorted_arr)}
        for idx,num in enumerate(arr):
            arr[idx]=ranked_map[num]
        return arr