# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        nums = []
        while head:
            nums.append(head)
            head=head.next
        l,r = 0,len(nums)-1
        while l < r:
            nums[l].next = nums[r]
            l += 1

            if l == r:
                break

            nums[r].next = nums[l]
            r -= 1

        # Mark the end of the list
        nums[l].next = None
        