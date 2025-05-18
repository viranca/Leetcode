class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cross = 0
        moved = 0
        for i in range(len(nums)):
            
            if nums[i] < 0:
                if moved > 0 and -nums[i] == moved:
                    cross +=1
                moved += nums[i]
            else:
                if moved < 0 and nums[i] == -moved:
                    cross += 1
                moved += nums[i]
        return cross

            
    