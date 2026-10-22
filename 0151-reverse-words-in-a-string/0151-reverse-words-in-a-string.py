class Solution:
    def reverseWords(self, s: str) -> str:
        x = " ".join(s.split()[::-1])
        return x

        