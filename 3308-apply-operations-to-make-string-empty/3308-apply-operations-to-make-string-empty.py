class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        
        result = ""
        seen = set()
        
        # Traverse from right to left to capture the last occurrence
        for ch in reversed(s):
            if counts[ch] == max_freq and ch not in seen:
                result = ch + result
                seen.add(ch)
        
        return result