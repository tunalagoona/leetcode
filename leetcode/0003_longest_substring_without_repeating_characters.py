"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


#  O(n) time complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        counters = []
        counter = 0
        check = []
        for let in s:
            if let in check:
                counters.append(counter)
                start = check.index(let) + 1
                check = check[start:]
                check.append(let)
                counter = len(check)
            else:
                counter += 1
                check.append(let)
        counters.append(counter)
        max_counter = max(counters)
        return max_counter


# string = "abcabcbb"
# string = "pwwkew"
string = "dvdf"
s = Solution()
print(s.lengthOfLongestSubstring(string))
