"""
Strings / easy
Time complexity: O(n). Space complexity: O(1).
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s_int = 0
        s = s.split()
        print(s)
        if len(s) == 0:
            return 0
        for i in range(0, len(s[0])):
            print(f's[0][i] = {s[0][i]}')
            if not s[0][i].isnumeric():
                print('not numeric')
                if s[0][i] != '+' and s[0][i] != '-':
                    print(f'len(s[0][: i + 1]) = {len(s[0][: i + 1])}')
                    if len(s[0][: i + 1]) <= 1:
                        return 0
                    else:
                        if i != 0:
                            if s[0][i - 1].isnumeric():
                                s_int = s[0][: i]
                                print(f's_int = {s_int}')
                                break
                            else:
                                return 0
                else:
                    print('either + or -')
                    if i != 0:
                        if s[0][i - 1] == '+' or s[0][i - 1] == '-':
                            return 0
                        if s[0][i - 1].isnumeric():
                            s_int = s[0][: i]
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


if __name__ == "__main__":
    # st = "   -42"
    # st = "words and 987"
    # st = "4193 with words"
    st = "+-12"
    # st = ""
    # st = "  -0012a42"
    # st = "00000-42a1234"
    # st = "-abc"
    sol = Solution()
    print(sol.myAtoi(st))

