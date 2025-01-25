class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
            return False

        opening_brackets = ["(", "{", "["]
        closing_brackets = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i not in opening_brackets and len(stack)==0:
                return False
            if i in opening_brackets:
                stack.append(i)
            elif closing_brackets[i] == stack.pop():
                continue
            else:
                return False         
        return True
   



