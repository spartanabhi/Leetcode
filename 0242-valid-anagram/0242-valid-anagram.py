class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        print(list1)
        print(list2)
        if list1==list2:
            return True
        else:
            return False
        