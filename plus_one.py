"""
Array / easy
Time complexity: O(n). Space complexity: O(1).
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while i != -1:
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    digits[i - 1] += 1
                i -= 1
            else:
                return digits
        return digits


if __name__ == "__main__":
    numbers = [9, 9, 9]
    sol = Solution()
    print(sol.plusOne(numbers))
