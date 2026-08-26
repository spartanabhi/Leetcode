class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums),reverse = True)
        if len(nums)>=3:
            return nums[2]
        elif len(nums)<=2:
            if len(nums)==2:
                return nums[0]
            elif len(nums)==1:
                return nums[0]
            else:
                return