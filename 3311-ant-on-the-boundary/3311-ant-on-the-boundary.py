class Solution2:
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

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        #prefix sum approach
        cross = 0
        dist = [0]
        for i in range(1, len(nums)+1):
            dist.append(dist[i-1] + nums[i-1])
            if dist[i] == 0:
                cross += 1
        return cross
