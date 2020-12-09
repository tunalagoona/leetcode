"""
Strings / easy
Time complexity: O(n). Space complexity: O(n).
"""


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ls = len(s)
#         lt = len(t)
#         if ls != lt:
#             return False
#         s = sorted(s)
#         t = sorted(t)
#         if s == t:
#             print(True)
#             return True
#         print(False)
#         return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False

        s_memo = {}
        for i in range(0, ls):
            if s[i] in s_memo:
                s_memo[s[i]] += 1
            else:
                s_memo[s[i]] = 1

        t_memo = {}
        for j in range(0, lt):
            if t[j] in t_memo:
                t_memo[t[j]] += 1
            else:
                t_memo[t[j]] = 1

        for key in s_memo.keys():
            if key in t_memo:
                if s_memo[key] != t_memo[key]:
                    return False
            else:
                return False
        return True


if __name__ == "__main__":
    # a = "anagram"
    # b = "nagaram"
    a = 'a'
    b = 'b'
    sol = Solution()
    print(sol.isAnagram(a, b))
