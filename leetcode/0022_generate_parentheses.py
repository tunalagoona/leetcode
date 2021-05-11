"""
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(idx, state, left_count, right_count):
            if right_count < left_count:
                return

            if idx == 2 * n:
                result.append("".join(state))
                return
            else:
                if left_count != 0:
                    state.append("(")
                    dfs(idx + 1, state, left_count - 1, right_count)
                    state.pop()

                if right_count != 0:
                    state.append(")")
                    dfs(idx + 1, state, left_count, right_count - 1)
                    state.pop()

        dfs(0, [], n, n)
        return result
