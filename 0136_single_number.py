"""
https://leetcode.com/problems/single-number/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def single_number(self, nums: List[int]) -> int:
        num = 0
        for i in range(0, len(nums)):
            num ^= nums[i]
        return num
