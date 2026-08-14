# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        lead = trail = dummy
        for _ in range(n):
            lead = lead.next
        while lead.next:
            lead = lead.next
            trail = trail.next
        trail.next = trail.next.next
        return dummy.next

        
        