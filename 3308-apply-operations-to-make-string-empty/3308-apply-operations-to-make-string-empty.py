class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        remove = counts.most_common()[0][1] - 1
        removals = [0] * 26
        
        ans = ''
        for i in range(len(s)):
            if removals[ord(s[i]) - ord('z')] < remove:
                removals[ord(s[i]) - ord('z')]+=1
            else:
                ans += s[i]
        return ans
        


