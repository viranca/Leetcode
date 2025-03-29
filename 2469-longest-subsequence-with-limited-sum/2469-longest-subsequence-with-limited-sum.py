class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        result = list()
        for target in queries:
            l, r = 0, len(nums) - 1
            found = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    found = mid
                    break
                elif nums[mid] < target:
                    found = mid
                    l = mid + 1
                else:
                    r = mid - 1
            result.append(found+1)
        return result