from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        max_profit = 0
        for c in prices:
            if c < low:
                low = c
            elif max_profit < c - low:
                max_profit = c -low
        return max_profit

