class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for elem in nums:
            ind = bisect_left(dp, elem)
            if ind == len(dp):
                dp.append(elem)
            else:
                dp[ind] = elem
        return len(dp)