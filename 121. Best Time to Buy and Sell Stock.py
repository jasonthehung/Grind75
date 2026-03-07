class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        max_profit = 0

        for p in prices:
            lowest = min(lowest, p)
            max_profit = max(max_profit, p - lowest)

        return max_profit
