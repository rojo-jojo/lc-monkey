# 121. Best time to buy and sell stocks

## Notes
- At every day update the minimum price yet
- calculate profit by subtracting current day's price from minimum price
- If the profit is greater than max profit yet update the max profit
  
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(profit, prices[i]-min_price)
        return profit
```
