class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))

        rank_dict = {}
        rank = 1
        for num in nums:
            rank_dict[num] = rank
            rank+=1

        for i in range(len(arr)):
            arr[i] = rank_dict[arr[i]]
        return arr 

        
