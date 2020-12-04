"""
Strings / easy
Time Complexity: O(log(x)). Space Complexity: O(1).
"""


class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = - 2 ** 31
        rev_x = 0

        if x < 0:
            while x != 0:
                rem = abs(x) % 10
                x = int(x / 10)
                if rev_x < int_min / 10 or rev_x == int_min / 10 and rem > 8:
                    return 0
                rev_x = rev_x * 10 - rem
        else:
            while x != 0:
                rem = abs(x) % 10
                x = int(x / 10)
                if rev_x > int_max / 10 or rev_x == int_max / 10 and rem > 7:
                    return 0
                rev_x = rev_x * 10 + rem
        return rev_x


if __name__ == "__main__":
    num = - 2147483648
    sol = Solution()
    sol.reverse(num)
