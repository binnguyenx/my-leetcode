class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low = prices[0]
        high = prices[0]
        profit = 0
        i = 0
        while i < n - 1:
            #dùng để chặn dưới, check dấu bé
            while i < n - 1 and prices[i] >= prices[i+1]:
                i += 1
            low = prices[i]
            #dùng để chặn trên, check dấu lớn
            while i < n - 1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]
            profit += high - low
        return profit