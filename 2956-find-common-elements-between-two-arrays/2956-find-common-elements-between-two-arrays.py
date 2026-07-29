class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        left = sum(1 for x in nums1 if x in set2)
        right = sum(1 for x in nums2 if x in set1)

        return [left, right]