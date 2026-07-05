class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = []

        for i in range(0,len(prices)-1):
            
            if prices[i] < prices[i+1]:
                if len(buy) == 0:
                    buy.append(prices[i])
                elif prices[i] < buy[0]:
                    buy[0] = prices[i]    
        
            elif (prices[i] > prices[i+1]):
                if len(buy) != 0:
                    if prices[i] - buy[0] > profit:
                        profit = prices[i] - buy[0]

        if len(buy)!=0:
            if prices[-1] - buy[0] > profit:
                profit = prices[-1] - buy[0]

        return profit                
