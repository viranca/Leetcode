class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        length_ = len(wordsDict)
        p1, p2 = -1, -1
        min_distance = length_
        
        for i in range(length_):
            
            if wordsDict[i] == word1:
                p1 = i
                
            if wordsDict[i] == word2:
                p2 = i
                 
            if p1 != -1 and p2 != -1:       
                min_distance =  min(min_distance, abs(p1-p2))
                
        return min_distance