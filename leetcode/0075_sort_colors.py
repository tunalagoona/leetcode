"""
https://leetcode.com/problems/sort-colors/
"""
from typing import List


class Solution:
    def sortColors(self, nums: List) -> None:
        i, j, k = 0, 0, 0
        for num in nums:
            if num == 0:
                i += 1
            if num == 1:
                j += 1
            if num == 2:
                k += 1

        nums.clear()
        for ind in range(i):
            nums.append(0)
        for ind in range(j):
            nums.append(1)
        for ind in range(k):
            nums.append(2)


ns = [2, 0, 2, 1, 1, 0]
s = Solution()
s.sortColors(ns)
print(ns)
