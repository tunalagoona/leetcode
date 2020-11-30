from typing import List


class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        max_wealth = 0
        for i in range(0, m):
            n = len(accounts[i])
            cust_wealth = 0
            for j in range(0, n):
                cust_wealth += accounts[i][j]
            if cust_wealth > max_wealth:
                max_wealth = cust_wealth
        return max_wealth


if __name__ == "__main__":
    acc = [[1, 3], [7, 9]]
    s = Solution()
    print(s.maximum_wealth(acc))
