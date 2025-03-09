class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = []
        for row in edges:
            for node in row:
                if node in seen:
                    return node
                seen.append(node)
                

