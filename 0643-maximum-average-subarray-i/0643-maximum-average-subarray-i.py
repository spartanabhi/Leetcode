
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        avg = nums[0]
        sums = 0
        for i in range(k):
            sums+=nums[i]
        max_sum = sums
        for right in range(k,len(nums)):
            sums += nums[right]
            sums-=nums[left]
            max_sum = max(sums,max_sum)
            left+=1
        return max_sum/k
            
            


        