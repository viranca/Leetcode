class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common(k)
        ans = [key[0] for key in counts[:k]]
        return ans
        =-\