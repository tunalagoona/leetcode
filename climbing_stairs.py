# level: easy


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        comb_num = [0] * (n + 1)
        comb_num[1] = 1
        comb_num[2] = 2
        for num in range(3, n + 1):
            comb_num.append(0)
            comb_num[num] = comb_num[num - 1] + comb_num[num - 2]
        # print(comb_num[num])
        return comb_num[n]


if __name__ == "__main__":
    numb = int(input('n = '))
    s = Solution()
    s.climb_stairs(numb)
