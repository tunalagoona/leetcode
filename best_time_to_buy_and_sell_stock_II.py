"""
Array / easy
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.calculate(prices, 0)

    def calculate(self, prices, s):
        l = len(prices)
        if s >= l - 1:
            return 0
        maximum = 0
        for start in range(s, l):
            max_profit = 0
            for i in range(start + 1, l):
                if prices[start] < prices[i]:
                    profit = self.calculate(prices, i + 1) + prices[i] - prices[start]
                    if profit > max_profit:
                        max_profit = profit

            if max_profit > maximum:
                maximum = max_profit
        return maximum


if __name__ == "__main__":
    pr = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    sol.maxProfit(pr)
