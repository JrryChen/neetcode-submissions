class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice, minPrice, profit = prices[0], prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice, maxPrice = prices[i], prices[i]
            if prices[i] > maxPrice:
                maxPrice = prices[i]
                profit = max(profit, maxPrice - minPrice)

        return profit            