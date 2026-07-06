class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            profit = prices[i] - buy
            max_profit = max(profit,max_profit)
            buy = min(prices[i],buy)

        return max_profit    