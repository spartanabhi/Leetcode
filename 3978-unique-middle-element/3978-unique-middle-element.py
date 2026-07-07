class Solution(object):
    def isMiddleElementUnique(self, nums):
        middle = nums[len(nums)//2]
        count = 0
        for i in range(len(nums)):
            if nums[i]==middle:
                count+=1
        if count>1:
            return False
        else:
            return True
        
        