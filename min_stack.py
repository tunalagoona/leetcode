"""
Design / easy
Time complexity of each method: O(1).
"""


# class MinStack:
#
#     def __init__(self):
#         self.array = []
#         self.min = [float('inf')]
#
#     def push(self, x: int) -> None:
#         self.array.append(x)
#         self.min.append(x)
#         self.min.sort()
#
#     def pop(self) -> None:
#         self.min.remove(self.array[-1])
#         del self.array[-1]
#
#     def top(self) -> int:
#         return self.array[-1]
#
#     def getMin(self) -> int:
#         return self.min[0]

class MinStack:

    def __init__(self):
        self.array = []
        self.length = 0

    def push(self, x: int) -> None:
        if self.length == 0 or x < self.array[-1][1]:
            self.array.append([x, x])
        else:
            self.array.append([x, self.array[-1][1]])
        self.length += 1

    def pop(self) -> None:
        self.length -= 1
        self.array.pop()

    def top(self) -> int:
        return self.array[-1][0]

    def getMin(self) -> int:
        return self.array[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    print(obj.getMin())
    obj.push(0)
    obj.push(-1)
    print(obj.getMin())
    print(obj.top())
    obj.pop()
    print(obj.getMin())
