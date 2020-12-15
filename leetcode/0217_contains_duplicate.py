"""
https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        memo = {}
        for i in range(0, len(nums)):
            if nums[i] in memo:
                return True
            else:
                memo[nums[i]] = 0
        return False
