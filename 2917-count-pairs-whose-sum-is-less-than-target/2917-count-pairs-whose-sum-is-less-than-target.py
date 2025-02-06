class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i=0
        score = 0
        for i in range(len(nums)): 
            for j in range(len(nums)):
                if j > i:
                    if nums[i] + nums[j] < target:
                        score+=1
        
        return score 