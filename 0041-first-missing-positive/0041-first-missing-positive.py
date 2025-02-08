class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not 1 in nums:
            return 1
        else:
            for i in range(len(nums)-1):
                if nums[i+1] != nums[i] + 1 and nums[i]>0:
                    return nums[i]+1
        if (nums[-1] + 1) > 0:
            return nums[-1] + 1
        else:
            return 1