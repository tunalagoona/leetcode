"""
https://leetcode.com/problems/number-of-1-bits/
"""


# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def hamming_weight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += 1
            n &= (n - 1)
        return s
