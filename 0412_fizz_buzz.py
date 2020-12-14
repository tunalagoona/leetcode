"""
https://leetcode.com/problems/fizz-buzz/
"""

from typing import List


# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def fizz_buzz(self, n: int) -> List[str]:
        result = []
        for k in range(1, n + 1):
            ans = ''
            divisible_by_3 = (k % 3 == 0)
            divisible_by_5 = (k % 5 == 0)

            if divisible_by_3:
                ans += "Fuzz"
            if divisible_by_5:
                ans += "Buzz"
            if not divisible_by_3 and not divisible_by_5:
                ans = str(k)
            result.append(ans)

        return result
