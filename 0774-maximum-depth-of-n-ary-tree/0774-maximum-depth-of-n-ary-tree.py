"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        queue=[]
        queue.append(root)
        depth=0
        while(len(queue)!=0):
            l=len(queue)
            for i in range(l):
                cur=queue.pop(0)
                for nodes in cur.children:
                    queue.append(nodes)
            depth+=1
        return depth