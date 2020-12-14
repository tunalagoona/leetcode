"""
https://leetcode.com/problems/shuffle-an-array/
"""


from typing import List
from random import randint


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.initial = nums.copy()

    def reset(self) -> List[int]:
        return self.initial

    # time complexity: O(n)
    # space complexity: O(1)
    def shuffle(self) -> List[int]:
        length = len(self.arr)
        for i in range(0, length):
            j = randint(i, length - 1)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
