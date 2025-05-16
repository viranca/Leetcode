class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = Counter(s)

        if len(counts) <= k:
            return 0

        freq = sorted(counts.values())

        deletions = sum(freq[:len(freq) - k])

        return deletions
