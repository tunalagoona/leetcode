"""
https://leetcode.com/problems/plus-one/
"""
from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
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
