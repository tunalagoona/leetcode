"""
Array / easy
Solution with a memo set
Time complexity: O(n). Space complexity: O(n).
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = set()
        for i in range(0, len(nums)):
            if target - nums[i] in memo:
                return [i, nums.index(target - nums[i])]
            memo.add(nums[i])


if __name__ == "__main__":
    # numbers = [1, 27, 2, 29, 8, 5]
    numbers = [3, 3]
    target = 6
    sol = Solution()
    print(sol.twoSum(numbers, target))
