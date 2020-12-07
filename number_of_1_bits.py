"""
Others / easy
"""


class Solution:
    # def hamming_weight(self, n: int) -> int:
    #     bin_n = bin(n)
    #     count = 0
    #     bin_n = bin_n[2:]
    #     print(bin_n)
    #     for b in str(bin_n):
    #         if int(b) == 1:
    #             count += 1
    #     print(count)
    #     return count

    def hamming_weight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += 1
            n &= (n - 1)
        print(s)
        return s


if __name__ == "__main__":
    num = 9
    s = Solution()
    s.hamming_weight(num)
