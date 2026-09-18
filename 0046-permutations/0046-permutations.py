from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        for p in permutations(nums):
            res.append(list(p))
        return res