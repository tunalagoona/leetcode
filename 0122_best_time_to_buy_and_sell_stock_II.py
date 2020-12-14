"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

