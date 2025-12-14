class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            cost = prices[i]-minprice
            profit = max(profit,cost)
            minprice = min(minprice,prices[i])
        
        return profit
        