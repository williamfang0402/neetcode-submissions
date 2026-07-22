class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDate = 0
        sellDate = 1
        max_profit = 0
        
        while sellDate < len(prices):
            if prices[sellDate] < prices[buyDate]:
                buyDate = sellDate
            else:
                max_profit = max(max_profit, prices[sellDate]-prices[buyDate])
            sellDate += 1

        return max_profit