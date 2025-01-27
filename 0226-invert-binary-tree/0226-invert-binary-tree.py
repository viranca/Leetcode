class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # Base case: If the tree is empty, return None.

        q = deque([root])  # Queue for level-order traversal.
        while q:
            node = q.popleft()  # Process the current node.

            # Swap the left and right children.
            node.left, node.right = node.right, node.left
            
            # Add the children to the queue if they exist.
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root  # Return the root of the inverted tree.