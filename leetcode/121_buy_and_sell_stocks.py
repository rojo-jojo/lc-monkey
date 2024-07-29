class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(profit, prices[i]-min_price)
        return profit