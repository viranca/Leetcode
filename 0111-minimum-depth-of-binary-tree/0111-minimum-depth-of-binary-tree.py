# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def recurse(node):
            if node is None:
                return 0
            if node.left is None:
                return 1 + recurse(node.right)
            elif node.right is None:
                return 1 + recurse(node.left)
            return min(recurse(node.left), recurse(node.right)) + 1
        
        return recurse(root)