"""
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self.array = []
        self.length = 0

    # time complexity: O(1)
    def push(self, x: int) -> None:
        if self.length == 0 or x < self.array[-1][1]:
            self.array.append([x, x])
        else:
            self.array.append([x, self.array[-1][1]])
        self.length += 1

    # time complexity: O(1)
    def pop(self) -> None:
        self.length -= 1
        self.array.pop()

    # time complexity: O(1)
    def top(self) -> int:
        return self.array[-1][0]

    # time complexity: O(1)
    def get_min(self) -> int:
        return self.array[-1][1]
