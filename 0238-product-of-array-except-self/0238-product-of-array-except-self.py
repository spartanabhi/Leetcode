class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= arr[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= arr[i]
        return result
        