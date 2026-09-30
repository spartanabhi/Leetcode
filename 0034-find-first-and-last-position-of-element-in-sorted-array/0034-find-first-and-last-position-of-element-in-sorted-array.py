class Solution:

    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # Brute force
        # first = -1
        # last = -1
        #
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i
        #
        # return [first, last]


        # Better - Two pointers
        # if len(nums) == 0:
        #     return [-1, -1]
        #
        # l, r = 0, len(nums) - 1
        #
        # while l <= r:
        #     if nums[l] == target and nums[r] == target:
        #         return [l, r]
        #
        #     if nums[l] < target:
        #         l += 1
        #
        #     if nums[r] > target:
        #         r -= 1
        #
        # return [-1, -1]


        # Optimal - Two Binary Searches

        # Find first occurrence
        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Find last occurrence
        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first, last]