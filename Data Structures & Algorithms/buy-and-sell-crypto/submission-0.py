class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0

        lowest = 101
        min_on_left = [0]*len(prices)
        min_on_left[0] = prices[0]
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i-1])
            min_on_left[i] = lowest


        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-min_on_left[i])
        return max_profit