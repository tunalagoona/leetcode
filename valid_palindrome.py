"""
Strings / easy
Time complexity: O(n). Space complexity: O(1).
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
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


if __name__ == "__main__":
    # a = "A man, a plan, a canal: Panama"
    a = "race a car"
    sol = Solution()
    print(sol.isPalindrome(a))
