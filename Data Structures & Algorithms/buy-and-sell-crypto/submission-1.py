class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 0
        plowest = 0
        highest = 0
        profit = 0
        for i in range(len(prices)):
            if i != 0:
                if prices[i] < prices[plowest]:
                    plowest = i
                if prices[i] - prices[plowest] > profit:
                    highest = i
                profit = prices[highest] - prices[lowest]
                if prices[highest] - prices[plowest] > profit and highest > plowest:
                    lowest = plowest
                profit = prices[highest] - prices[lowest]
        return profit