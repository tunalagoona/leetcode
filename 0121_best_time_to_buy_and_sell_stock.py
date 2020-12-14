"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)
        valley = float("inf")
        max_profit = 0

        for i in range(0, length):
            if prices[i] < valley:
                valley = prices[i]

            elif prices[i] > valley:
                profit = prices[i] - valley
                if profit > max_profit:
                    max_profit = profit

        return max_profit
