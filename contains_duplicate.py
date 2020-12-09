"""
Array / easy
Time complexity: O(n). Space complexity: O(n).
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for i in range(0, len(nums)):
            if nums[i] in memo:
                return True
            else:
                memo[nums[i]] = 0
        return False


if __name__ == "__main__":
    numbers = [1, 2, 3, 1]
    sol = Solution()
    sol.containsDuplicate(numbers)
