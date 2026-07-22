class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = prices[0]
        sell = 0
        for price in prices:
            if price > buy:
                sell = price
                if (sell-buy) > profit:
                    profit = sell-buy
            elif price < buy:
                buy = price

        return profit        