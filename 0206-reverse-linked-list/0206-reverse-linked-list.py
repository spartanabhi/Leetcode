class Solution:
    def reverseList(self, head):
        arr = []

        # Linked List → Array
        while head:
            arr.append(head.val)
            head = head.next

        # Array → Linked List
        dummy = ListNode(0)
        curr = dummy

        for val in reversed(arr):
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
    
    