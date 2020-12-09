"""
Array / easy
Time complexity: O(n). Space complexity: O(1).
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(0, len(nums)):
            num ^= nums[i]
        print(num)
        return num


if __name__ == "__main__":
    numbers = [2, 2, 1, 3, 3, 4, 1]
    sol = Solution()
    sol.singleNumber(numbers)
