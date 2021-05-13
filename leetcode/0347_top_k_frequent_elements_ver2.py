"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
import heapq
from typing import List
from collections import Counter


# O(n log k) time complexity
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
