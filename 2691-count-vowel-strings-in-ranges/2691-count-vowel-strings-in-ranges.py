class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a','e','i','o','u'])

        if words[0][0] in vowels and words[0][-1] in vowels:
            words[0] = 1
        else:
            words[0] = 0
                
        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                words[i] = words[i-1] + 1
            else:
                words[i] = words[i-1]

        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(words[r])
            else:
                ans.append(words[r] - words[l - 1])
        
        return ans



