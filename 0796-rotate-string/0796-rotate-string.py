class Solution:
    def rotateString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        else:
            return True if s2 in (s1 + s1) else False
        