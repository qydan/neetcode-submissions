class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        highest = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                highest = max(highest, curr)
            else:
                l = r
            r+=1
        return highest