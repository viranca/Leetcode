class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg_list = []
        while nums:
            avg = (min(nums) + max(nums))/2
            avg_list.append(avg)
            nums.pop(nums.index(min(nums)))
            nums.pop(nums.index(max(nums)))
        return len(set(avg_list))