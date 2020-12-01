from typing import List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.initial = nums.copy()  # O(n) time and space complexity

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        print(f'reset: {self.initial}')
        return self.initial

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = len(self.arr)
        for i in range(0, l):  # O(n) time complexity, O(1) space complexity
            j = randint(i, l - 1)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        print(f'shuffle: {self.arr}')
        return self.arr


if __name__ == "__main__":
    numbers = [1, 4, 6]
    obj = Solution(numbers)
    obj.reset()
    obj.shuffle()
    obj.reset()
    obj.shuffle()

