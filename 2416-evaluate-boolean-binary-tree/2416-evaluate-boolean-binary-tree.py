# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def evaluate(node):
            if node.val == 0:
                return False
            elif node.val == 1:
                return True

            elif node.val == 2:
                if evaluate(node.left) or evaluate(node.right):
                    return True
                else:
                    return False

            elif node.val == 3:
                if evaluate(node.left) and evaluate(node.right):
                    return True
                else:
                    return False

        return evaluate(root)