"""
Others / easy
Time complexity: O(1). Space complexity: O(1).
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        mask = 0b1
        while mask <= x or mask <= y:
            print(f'x & mask = {x & mask}')
            print(f'y & mask = {y & mask}')
            if x & mask != y & mask:
                count += 1
            mask = mask << 1
            print(f'mask = {mask}')
        print(count)
        return count


if __name__ == "__main__":
    a = 1
    b = 4
    sol = Solution()
    sol.hammingDistance(a, b)
