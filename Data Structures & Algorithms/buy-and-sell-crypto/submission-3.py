import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = (-1,math.inf)
        sell = (-1,0)

        if len(prices)==1:
            return 0

        if len(prices)==2:    
            return max([prices[1]-prices[0],0])
            
        for i in range(1,len(prices)-1):

            if prices[i-1] < prices[i] and prices[i-1] < buy[1]:
                buy = (i-1,prices[i-1])
                sell = (-1,0)
            elif prices[i] < buy[1]:
                buy = (i,prices[i])
                sell = (-1,0)

            if prices[i+1] > prices[i] and prices[i+1] > sell[1]:
                sell = (i+1,prices[i+1])
            elif prices[i] > sell[1]:
                sell = (i,prices[i])  

            profit = sell[1] - buy[1] if sell[1] - buy[1] > profit else profit

        return profit                   