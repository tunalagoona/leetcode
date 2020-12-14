"""
https://leetcode.com/problems/hamming-distance/
"""


# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        count = 0
        mask = 0b1
        while mask <= x or mask <= y:
            if x & mask != y & mask:
                count += 1
            mask = mask << 1
        return count

