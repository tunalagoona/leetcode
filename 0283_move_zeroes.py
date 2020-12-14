"""
https://leetcode.com/problems/move-zeroes/
"""

from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == 0:
                if nums[i] != 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            else:
                left += 1
