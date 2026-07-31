
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        result = -1
        for ch in range(len(s)):
            if freq[s[ch]]==1:
                result = ch
                break
        return result