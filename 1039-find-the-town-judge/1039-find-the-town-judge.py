class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        counter_trusted, counter_trustee = [0]*(n + 1), [0]*(n + 1)

        for relationship in trust:
            counter_trusted[relationship[1]] += 1
            counter_trustee[relationship[0]] += 1
        
        max_trusted = max(counter_trusted)
        if max_trusted == (n-1):
            if counter_trustee[counter_trusted.index(max_trusted)] == 0:
                return counter_trusted.index(max_trusted)
        return -1
 
