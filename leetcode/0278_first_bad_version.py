"""
https://leetcode.com/problems/first-bad-version/
"""


def is_bad_version(version):
    if version % 4 == 0:
        return True
    else:
        return False


# time complexity : O(log n)
# space complexity : O(1)
class Solution:
    def first_bad_version(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.first_bad(1, n, n)

    def first_bad(self, low, high, first):
        if low > high:
            first = low
            return first
        m = low + (high - low + 1) // 2
        if is_bad_version(m):
            if low == high:
                first = low
                return first
            first = self.first_bad(low, m - 1, m)
        else:
            if low == high:
                return first
            first = self.first_bad(m + 1, high, first)
        return first
