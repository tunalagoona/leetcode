"""
https://leetcode.com/problems/palindrome-number/
"""


# time complexity: O(n), where n - number of digits in input number
# space complexity: O(1)
class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + (x % 10)
            x = x // 10
        if x == reverted or reverted // 10 == x:
            return True
        else:
            return False


number = 120
s = Solution()
print(s.is_palindrome(number))
