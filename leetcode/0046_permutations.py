"""
https://leetcode.com/problems/permutations/
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(idx, state: List, rest_nums: List) -> None:
            if idx == len(nums):
                results.append([*state])
                return
            else:
                for num in rest_nums:
                    state.append(num)
                    new_nums = rest_nums.copy()
                    new_nums.remove(num)

                    dfs(idx + 1, state, new_nums)
                    state.pop()

        dfs(0, [], nums.copy())

        return results
