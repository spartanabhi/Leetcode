from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)

        if k > len(s2):
            return False

        # Frequency of s1
        need = Counter(s1)

        # First window
        test = s2[:k]
        window = Counter(test)

        if window == need:
            return True

        # Slide window
        for right in range(k, len(s2)):

            # Remove left character
            left = right - k
            window[s2[left]] -= 1

            # Add right character
            window[s2[right]] += 1

            # Check frequency
            if window == need:
                return True

        return False