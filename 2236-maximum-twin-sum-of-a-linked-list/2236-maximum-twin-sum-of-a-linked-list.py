# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        values = []

        while node:
            values.append(node.val)
            node = node.next
        
        print(values)
        maxsum = float(-inf)
        length = len(values)-1
        for i in range(length):
            maxsum = max(maxsum, values[i] + values[length-i])
        return maxsum
