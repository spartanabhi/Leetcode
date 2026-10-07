from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):

        result = []

        k = len(p)

        # If p is longer than s, anagram is impossible
        if k > len(s):
            return result

        # Frequency of characters required
        need = Counter(p)

        # Frequency of characters in current window
        window = Counter(s[:k])

        # Check the first window
        if window == need:
            result.append(0)

        # Slide the window
        for right in range(k, len(s)):

            # Add the new character entering the window
            window[s[right]] += 1

            # Remove the old character leaving the window
            left = right - k
            window[s[left]] -= 1

            # Remove character if its count becomes zero
            if window[s[left]] == 0:
                del window[s[left]]

            # Check whether current window is an anagram
            if window == need:
                result.append(left + 1)

        return result