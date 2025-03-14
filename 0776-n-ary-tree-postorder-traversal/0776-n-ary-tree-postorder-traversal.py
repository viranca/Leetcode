"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
            
        node_vals = []
        def get_child(node):
            
            if not node.children:
                node_vals.append(node.val)
                
            else:
                for child in node.children:
                    get_child(child)

                node_vals.append(node.val)
            
            return node_vals

        return get_child(root)  
        
    
        
            