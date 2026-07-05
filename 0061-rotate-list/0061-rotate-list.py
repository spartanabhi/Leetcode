class Solution(object):
    def rotateRight(self, head, k):

        if head is None or head.next is None:
            return head

        nums = []

        while head:
            nums.append(head)
            head = head.next

        n = len(nums)
        k = k % n

        if k == 0:
            return nums[0]

        # Connect last node to first node
        nums[-1].next = nums[0]

        # Break the list at the new tail
        nums[n - k - 1].next = None

        # Return the new head
        return nums[n - k]