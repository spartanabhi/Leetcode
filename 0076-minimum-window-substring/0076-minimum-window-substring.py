from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Frequency of characters required from t
        need = Counter(t)

        # Frequency of characters inside current window
        window = {}

        left = 0

        # Number of different characters whose required
        # frequency has been completely satisfied
        have = 0

        # Number of different characters we need to satisfy
        required = len(need)

        # Best answer
        min_length = float("inf")
        answer = ""

        # Expand window using right pointer
        for right in range(len(s)):

            # Add current character
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # If this character has now reached the
            # required frequency
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Window is valid
            while have == required:

                # Current window length
                length = right - left + 1

                # Save it if it is smaller
                if length < min_length:
                    min_length = length
                    answer = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # If removing it makes the window invalid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                # Move left pointer
                left += 1

        return answer