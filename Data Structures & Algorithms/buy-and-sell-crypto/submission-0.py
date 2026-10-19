class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if (n == 0): return 0

        max_profit = 0

        lowest_buy = prices[0]
        i = 1

        while i < n:
            max_profit = max(max_profit, prices[i] - lowest_buy)
            lowest_buy = min(lowest_buy, prices[i])

            i += 1
            
        
        return max_profit

        