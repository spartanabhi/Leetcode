class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num -1 not in num_set:
                leng = 1
                while num + leng in num_set:
                    leng += 1
                longest = max(longest,leng)

        return longest