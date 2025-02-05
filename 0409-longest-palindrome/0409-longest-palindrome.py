class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = {}

        for c in s:
            freq_map[c] = freq_map.get(c,0) + 1
        
        res = 0
        has_odd = False
        for freq in freq_map.values():
            if (freq % 2) == 0:
                res += freq
            else:
                res += freq - 1
                has_odd = True
        
        if has_odd:
            return res+1
        return res