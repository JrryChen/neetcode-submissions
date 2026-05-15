class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxPrice, profit = prices[0], prices[0], 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
               minPrice, maxPrice = prices[i], prices[i]
            else:
                maxPrice = prices[i]
                profit = max(profit, maxPrice - minPrice)
                    
        return profit