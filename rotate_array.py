"""
Array / easy
Time complexity: O(k * n). Space complexity: O(1).
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(0, k):
            x = nums[0]
            for i in range(0, len(nums) - 1):
                y = nums[i + 1]
                nums[i + 1] = x
                x = y
            nums[0] = x
        print(nums)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    rotate_by = 3
    sol = Solution()
    sol.rotate(numbers, rotate_by)
