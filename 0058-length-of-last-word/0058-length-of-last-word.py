class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.split()
        x = y[-1]
        z = list(x)
        return len(z)
        