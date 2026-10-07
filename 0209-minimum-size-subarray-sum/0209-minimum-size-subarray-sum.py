class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = 0
        current = 0
        min_wind = float("inf")

        for right in range(len(nums)):

            # Add current element
            current += nums[right]

            # Keep shrinking while sum is enough
            while current >= target:

                # Current window is valid
                min_wind = min(min_wind, right - left + 1)

                # Remove left element
                current -= nums[left]
                left += 1

        # If no valid subarray was found
        if min_wind == float("inf"):
            return 0

        return min_wind