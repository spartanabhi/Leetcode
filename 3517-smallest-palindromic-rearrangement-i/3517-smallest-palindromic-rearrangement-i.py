class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left = []
        middle = ''

        for char in sorted(count):
            left.append(char * (count[char] // 2))

            if count[char] % 2 == 1:
                middle = char

        left = ''.join(left)

        return left + middle + left[::-1]