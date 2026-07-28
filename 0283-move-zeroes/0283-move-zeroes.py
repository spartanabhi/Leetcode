class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                arr.pop(i)
                arr.append(0)