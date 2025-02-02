class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if target in set(nums):
            return nums.index(target)
        else:
            return -1           