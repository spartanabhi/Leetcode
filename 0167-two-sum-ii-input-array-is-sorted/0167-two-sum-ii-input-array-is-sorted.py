class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        b , e = 0, len(numbers)-1
        while b<e:
            total = numbers[b]+numbers[e]
            if total == target:
                return [b+1,e+1]
            if total < target:
                b+=1
            else:
                e-=1

        