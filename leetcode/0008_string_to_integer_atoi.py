"""
https://leetcode.com/problems/string-to-integer-atoi/
"""


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def my_atoi(self, s: str) -> int:
        s_int = 0
        s = s.split()
        if len(s) == 0:
            return 0

        for i in range(0, len(s[0])):
            if not s[0][i].isnumeric():
                if s[0][i] != "+" and s[0][i] != "-":
                    if len(s[0][: i + 1]) <= 1:
                        return 0
                    else:
                        if i != 0:
                            if s[0][i - 1].isnumeric():
                                s_int = s[0][:i]
                                break
                            else:
                                return 0
                else:
                    if i != 0:
                        if s[0][i - 1] == "+" or s[0][i - 1] == "-":
                            return 0
                        if s[0][i - 1].isnumeric():
                            s_int = s[0][:i]
                            break
            else:
                s_int = s[0][: i + 1]

        if s_int != 0:
            s_int = int(s_int)
            if s_int > 2147483647:
                s_int = 2147483647
            if s_int < int(-2147483648):
                s_int = -2147483648

        return s_int
