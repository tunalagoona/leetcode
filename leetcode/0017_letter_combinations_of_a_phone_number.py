"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        if digits == "":
            return []

        results = []

        def dfs(idx: int, state: List[str]):
            if idx == len(digits):
                results.append("".join(state))
            else:
                letters = digits_to_letters[int(digits[idx])]

                for letter in letters:
                    state.append(letter)
                    dfs(idx + 1, state)
                    state.pop()

        dfs(idx=0, state=[])
        return results
