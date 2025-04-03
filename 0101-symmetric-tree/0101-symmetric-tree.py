# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        node = root
        
        def check_sym(node_left, node_right):
            if node_left is None and node_right is None:
                return True
            if node_left is None or node_right is None:
                return False
            return (
                (node_left.val == node_right.val)
                and check_sym(node_left.left, node_right.right)
                and check_sym(node_left.right, node_right.left)
            )

        return check_sym(node.left, node.right)