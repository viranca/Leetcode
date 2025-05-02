class Solution:
    def minimumPushes(self, word: str) -> int:
        sorted_counts = Counter(word).most_common()

        ans = 0
        for i in range(len(sorted_counts)):
            multiplier = i//8 + 1
            ans += multiplier * sorted_counts[i][1]
        return ans
