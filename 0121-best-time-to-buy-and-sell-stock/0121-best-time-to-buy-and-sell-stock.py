class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_p = 0

        for price in prices[1:]:

            max_p = max(max_p , price-min_p)
            min_p = min(price,min_p)
        return max_p
        