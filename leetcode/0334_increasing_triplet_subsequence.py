"""
https://leetcode.com/problems/increasing-triplet-subsequence/
"""
from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        cur_max = -math.inf
        cur_mid = -math.inf

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < cur_mid:
                return True
            if nums[i] > cur_max:
                cur_max = nums[i]
            if nums[i] < cur_max:
                cur_mid = nums[i]
        return False
