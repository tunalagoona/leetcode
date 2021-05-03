"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


#  O(n**2) time complexity
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def grow(idx: int, ext: int) -> str:
            l_ptr = idx
            r_ptr = idx + ext

            while l_ptr >= 0 and r_ptr < len(s) and s[l_ptr] == s[r_ptr]:
                l_ptr -= 1
                r_ptr += 1

            return s[l_ptr + 1 : r_ptr]

        def max_str(a: str, b: str) -> str:
            return a if len(a) > len(b) else b

        max_palindrome = ""

        for i in range(len(s)):
            max_palindrome = max_str(grow(i, ext=0), max_palindrome)
            max_palindrome = max_str(grow(i, ext=1), max_palindrome)

        return max_palindrome
