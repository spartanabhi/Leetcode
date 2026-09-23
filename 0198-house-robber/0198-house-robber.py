class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, curr = 0,0
        for i in nums:
            prev , curr = curr, max(prev+i,curr)
        return curr
        