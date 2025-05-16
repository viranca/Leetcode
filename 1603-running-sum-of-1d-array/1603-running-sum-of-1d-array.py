class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            runsum[i] = runsum[i-1] + nums[i]
        return runsum

