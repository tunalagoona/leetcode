"""
https://leetcode.com/problems/reverse-string/
"""


# time complexity: O(n)
# space complexity: O(1)
def reverse_string(s):
    i, j = 0, len(s) - 1
    while True:
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
