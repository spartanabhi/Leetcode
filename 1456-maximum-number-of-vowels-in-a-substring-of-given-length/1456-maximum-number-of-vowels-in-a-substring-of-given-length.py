class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0 
        count = 0
        vowel = "aeiou"
        max_count = float("-inf")
        if not s :
            return 0
        if len(s)<=k:
            for i in range(len(s)):
                if s[i] in vowel:
                    count+=1
            return count
        for i in range(k):
            if s[i] in vowel:
                count+=1
        max_count = count
        for right in range(k,len(s)):
            if s[right] in vowel:
                count+=1
            if s[left] in vowel:
                count-=1
            max_count = max(count,max_count)
            left+=1
            
        return max_count
            

            
        