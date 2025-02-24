# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head
        
        while current:
            # Skip m-1 nodes to land on the m-th node
            for i in range(1, m):
                if current is None:
                    return head
                current = current.next
            
            # If we've reached the end of the list, break out
            if current is None:
                break
            
            # Start from the next node that needs deletion
            temp = current.next
            # Delete next n nodes
            for i in range(n):
                if temp is None:
                    break
                temp = temp.next
            
            # Connect the m-th node to the node after the deleted ones
            current.next = temp
            # Move current to continue from the next part of the list
            current = temp
        
        return head
