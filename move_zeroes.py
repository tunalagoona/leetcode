"""
Array / easy
Time complexity: O(n). Space complexity: O(1).
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == 0:
                if nums[i] != 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            else:
                left += 1
            print(f'nums = {nums}')


if __name__ == "__main__":
    # numbers = [0, 0, 1, 0, 2, 2, 0, 8]
    numbers = [1, 0, 1]
    sol = Solution()
    sol.moveZeroes(numbers)
