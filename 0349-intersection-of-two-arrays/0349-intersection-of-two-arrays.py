class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [i for i in set(nums1) if i in set(nums2)]