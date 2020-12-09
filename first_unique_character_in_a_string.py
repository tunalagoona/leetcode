"""
Strings / easy
Time complexity: O(n). Space complexity: O(1).
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        lt_cnt = {}
        for i in range(0, length):
            if s[i] in lt_cnt:
                lt_cnt[s[i]][0] += 1
            else:
                lt_cnt[s[i]] = [1, i]

        min_pos = float('inf')
        for key in lt_cnt.keys():
            if lt_cnt[key][0] == 1:
                if lt_cnt[key][1] < min_pos:
                    min_pos = lt_cnt[key][1]
        if min_pos == float('inf'):
            min_pos = -1
        return min_pos


if __name__ == "__main__":
    # st = 'leetcode'
    st = 'cc'
    sol = Solution()
    sol.firstUniqChar(st)
