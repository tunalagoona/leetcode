"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i = 0
        for j in range(1, length):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

