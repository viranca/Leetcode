class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        out = set()
        visited = set()

        for i in range(len(s)-9):
            if s[i:i+10] in visited:
                out.add(s[i:i+10])
            visited.add(s[i:i+10])

        return list(out)