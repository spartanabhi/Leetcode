class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        else:
            a, b = 1, 1 # ways(0), ways(1)
            for _ in range(2, n + 1):
                a, b = b, a + b
        return b

        