
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev,k)
            if kth is None:
                break
            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    def getKth(self,curr,k):
        while curr is not None and k>0:
            curr = curr.next
            k-=1
        return curr

