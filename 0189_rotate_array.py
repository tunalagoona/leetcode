"""
https://leetcode.com/problems/rotate-array/
"""
from typing import List


class Solution:
    def reverse(self, nums, start, end):
        nums[start], nums[end] = nums[end], nums[start]

    # time complexity: O(n)
    # space complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        nums.reverse()

        s = 0
        e = k - 1
        while s < e:
            self.reverse(nums, s, e)
            s += 1
            e -= 1

        s = k
        e = length - 1
        while s < e:
            self.reverse(nums, s, e)
            s += 1
            e -= 1
