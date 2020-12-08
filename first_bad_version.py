"""
Sorting and searching / easy
Time complexity : O(log n)
Space complexity : O(1)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer


def isBadVersion(version):
    if version % 4 == 0:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.first_bad(1, n, n)

    def first_bad(self, low, high, first):
        if low > high:
            print('low > high')
            first = low
            return first
        print(f'low = {low}, high = {high}, first bad = {first}')
        m = low + (high - low + 1) // 2
        print(f'm = {m}')
        if isBadVersion(m):
            if low == high:
                first = low
                return first
            first = self.first_bad(low, m - 1, m)
        else:
            if low == high:
                return first
            first = self.first_bad(m + 1, high, first)
        print(f'first bad = {first}')
        return first


if __name__ == '__main__':
    num = 9
    sol = Solution()
    sol.firstBadVersion(num)
