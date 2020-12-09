"""
Array / easy
"""
from typing import List

#
# class Solution:  # Time complexity: O(k * n). Space complexity: O(1).
#     def rotate(self, nums: List[int], k: int) -> None:
#         k = k % len(nums)
#         for _ in range(0, k):
#             x = nums[0]
#             for i in range(0, len(nums) - 1):
#                 y = nums[i + 1]
#                 nums[i + 1] = x
#                 x = y
#             nums[0] = x
#         print(nums)


class Solution:  # Time complexity: O(n). Space complexity: O(k)
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        y = {0: nums[0]}
        for i in range(0, length):
            print(f'i = {i}')
            if i not in y:
                y[i] = nums[i]
            print(f'y = {y}')
            ind = (i + k) % length
            x = nums[ind]
            nums[ind] = y[i]
            del y[i]
            y[ind] = x
            print(f'y = {y}')
            print(f'nums = {nums}')


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rotate_by = 3
    sol = Solution()
    sol.rotate(numbers, rotate_by)
