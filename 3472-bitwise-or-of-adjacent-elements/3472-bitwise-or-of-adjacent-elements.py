class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        result = []
        for x in range(0, len(nums) - 1):
            result.append((nums[x] | nums[x + 1]))
        return result