class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else: return None
        
        slow = head
        while fast != slow:
            slow, fast = slow.next, fast.next
            
        return slow