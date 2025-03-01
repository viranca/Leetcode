# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequency = {}
        freqHead = None
        while head:
            if head.val not in frequency:
                frequency[head.val] = ListNode(1, freqHead)
                freqHead = frequency[head.val]
            else:
                frequency[head.val].val += 1
            head = head.next
        
        return freqHead