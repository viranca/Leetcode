class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def flip(nums, i):
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
        
        flips = 0
        
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip(nums,i)
                flips += 1

        if sum(nums) == len(nums):
            return flips
        return -1

