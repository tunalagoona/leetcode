"""
Dynamic Programming / easy
Time complexity : O(n). Space complexity : O(1).
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        length = len(prices)
        valley = float('inf')
        max_profit = 0

        for i in range(0, length):
            if prices[i] < valley:
                valley = prices[i]

            elif prices[i] > valley:
                profit = prices[i] - valley
                if profit > max_profit:
                    max_profit = profit

        print(max_profit)
        return max_profit


if __name__ == "__main__":
    pr = [7, 1, 5, 3, 6, 4]
    # pr = [7, 6, 4, 3, 1]
    # pr = [1, 2]
    # pr = [2, 4, 1]
    sol = Solution()
    sol.maxProfit(pr)
