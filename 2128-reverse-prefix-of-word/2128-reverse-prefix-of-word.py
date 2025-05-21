class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ''
        stack = ''

        for i in range(len(word)):
            
            stack += word[i]
            if word[i] == ch:
                ans += stack[::-1]
                ans += word[i+1:]

                break
        if ans:
            return ans
        return word
            