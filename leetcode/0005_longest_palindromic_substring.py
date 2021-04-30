"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


#  O(n**2) time complexity
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        r, z, substring = len(s), 0, ""

        for i in range(r):
            if i == 0:
                if s[i] == s[i + 1]:
                    z = 2
                    substring = s[i : i + 2]
                else:
                    z = 1
                    substring = s[i]
                continue

            if i == r - 1:
                if z == 1:
                    substring = s[i]
                break

            if s[i] == s[i + 1]:
                length = 2
                if length >= z:
                    substring = s[i : i + 2]
                    z = length

                j = 1
                while i - j >= 0 and i + j + 1 <= r - 1:
                    if s[i - j] == s[i + j + 1]:
                        length += 2
                        if length >= z:
                            substring = s[i - j : i + j + 2]
                            z = length
                    else:
                        break
                    j += 1

            length = 1
            j = 1
            while i - j >= 0 and i + j <= r - 1:
                if s[i - j] == s[i + j]:
                    length += 2
                    if length >= z:
                        substring = s[i - j : i + j + 1]
                        z = length
                else:
                    break
                j += 1

        return substring
