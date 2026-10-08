class Solution:
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}
        
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            # We need an earlier prefix equal to prefix - k
            answer += prefix_count.get(prefix - k, 0)

            # Store this prefix sum
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1


        return answer