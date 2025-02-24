# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node = head
        vals = set()
        while node is not None:
            if node in vals:
                return True        
            vals.add(node)
            node = node.next
        return False
            


