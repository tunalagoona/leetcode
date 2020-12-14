"""
https://leetcode.com/problems/climbing-stairs/
"""


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        comb_num = [0] * (n + 1)
        comb_num[1] = 1
        comb_num[2] = 2
        for num in range(3, n + 1):
            comb_num.append(0)
            comb_num[num] = comb_num[num - 1] + comb_num[num - 2]
        return comb_num[n]
