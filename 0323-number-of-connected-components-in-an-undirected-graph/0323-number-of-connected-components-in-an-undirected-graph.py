from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list for the undirected graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        # Depth-First Search helper function
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        components = 0
        
        # Check each node; if not visited, it's a new component
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        
        return components