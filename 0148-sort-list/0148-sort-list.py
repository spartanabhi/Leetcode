# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
       
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    def getMid(self,head):
        prev = None
        while head is not None and head.next is not None:
            if prev == None:
                prev = head
            else:
                prev = prev.next
            head = head.next.next
        mid = prev.next
        prev.next = None
        return mid
    def merge(self,list1,list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next 
                

