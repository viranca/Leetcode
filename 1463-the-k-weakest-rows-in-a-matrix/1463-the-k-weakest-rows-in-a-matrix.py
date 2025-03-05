class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        print(strengths)
        return [i for strength, i in sorted(strengths)[:k]]