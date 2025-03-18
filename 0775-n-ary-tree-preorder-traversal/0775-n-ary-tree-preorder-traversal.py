"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        def traverse(node):
            children = []
            children.append(node.val)
            if node.children:
                for child in node.children:
                    children.extend(traverse(child))      
            return children      

        return traverse(root)


