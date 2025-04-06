# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def count_children(node):
            
            if node:
                self.count +=1
                count_children(node.left)
                count_children(node.right)
        
        count_children(root)

        return self.count