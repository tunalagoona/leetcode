"""
Others / easy
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        count = 0
        bin_n = bin_n[2:]
        print(bin_n)
        for b in str(bin_n):
            if int(b) == 1:
                count += 1
        print(count)
        return count


if __name__ == "__main__":
    num = 11
    s = Solution()
    s.hammingWeight(num)
