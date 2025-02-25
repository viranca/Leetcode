class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range(100000):
            if i not in set(arr):
                missing.append(i)
            if len(missing) == k +1:
                break
        return missing[-1]
        
