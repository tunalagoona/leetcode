"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        memo = set()
        for i in range(0, len(nums)):
            if target - nums[i] in memo:
                return [i, nums.index(target - nums[i])]
            memo.add(nums[i])
