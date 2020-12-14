"""
https://leetcode.com/problems/valid-palindrome/
"""


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def is_palindrome(self, s: str) -> bool:
        ls = len(s)
        if ls == 0:
            return True
        j = ls - 1
        i = 0
        while i < j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() != s[j].lower():
                        return False
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return True
