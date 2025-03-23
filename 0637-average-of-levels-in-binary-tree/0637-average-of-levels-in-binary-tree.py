# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        
        queue = collections.deque([root])
        level_avg = []
        
        while queue:
            level_sum = 0
            level_size = len(queue)


            for i in range(len(queue)):
                current = queue.popleft()
                level_sum += current.val
                
                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)

            level_avg.append(level_sum/level_size)

        return level_avg

        