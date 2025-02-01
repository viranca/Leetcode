class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(e for e in s if e.isalnum())
        return palindrome.lower() == palindrome.lower()[::-1]