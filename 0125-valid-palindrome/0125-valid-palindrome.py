class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(e for e in s if e.isalnum())
        return palindrome.lower() == palindrome.lower()[::-1]

    def isPalindrome_twopointer(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True