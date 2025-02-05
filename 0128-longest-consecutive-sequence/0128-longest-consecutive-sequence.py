class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        res = 1
        res_list = []
        for i in range(len(nums)-1):
            prev_num = nums[i]
            if nums[i+1] == prev_num + 1:
                res+=1

            else:
                res_list.append(res)
                res = 1
        res_list.append(res)
       
        return max(res_list)

