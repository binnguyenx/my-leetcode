class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        l = 0
        for r in range(1, n):
            #checking for the minimum of l
            if prices[r] < prices[l]:
                l = r
            else:
                curr_profit = prices[r] - prices[l]
                max_profit = max(curr_profit, max_profit)
        return max_profit