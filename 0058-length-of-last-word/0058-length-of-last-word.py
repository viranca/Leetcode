class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split(' ')
        for i in reversed(range(len(s_list))):
            if s_list[i] != '':
                return len(s_list[i])