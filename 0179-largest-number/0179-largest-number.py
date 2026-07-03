from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        asStrs = [str(num) for num in nums]
        def compare(a,b):
            order1 = a+b
            order2 = b+a
            if order2 > order1:
                return 1 
            elif order1 > order2:
                return -1 
            else:
                return 0
        asStrs.sort(key=cmp_to_key(compare))

        if asStrs[0]=='0':
            return '0'
        largestno = ""
        for i in asStrs:
            largestno += i
        return largestno


        