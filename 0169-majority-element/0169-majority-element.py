class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
