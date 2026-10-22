class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        left = 0
        right = len(x)-1
        while left<right:
            x[left],x[right] = x[right],x[left]
            left+=1
            right-=1
        reversed_sentence = " ".join(x)
        return reversed_sentence

        