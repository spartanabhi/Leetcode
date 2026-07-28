class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = -1
        for i in range(k):
            y = nums.pop(x)
            nums.insert(0,y)
            
        return nums
        