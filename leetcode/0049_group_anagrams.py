""""
https://leetcode.com/problems/group-anagrams/
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            s_sorted = sorted(s)
            string = "".join(s_sorted)
            if string in answer.keys():
                answer[string].append(s)
            else:
                answer[string] = [s]
        result = []
        for value in answer.values():
            result.append(value)
        return result
