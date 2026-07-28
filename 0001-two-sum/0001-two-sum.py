class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                result = [numMap[complement], i]
            numMap[nums[i]] = i

        return result if result else print -1  # No solution found