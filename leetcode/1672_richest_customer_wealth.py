"""
https://leetcode.com/problems/richest-customer-wealth/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
