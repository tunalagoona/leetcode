"""
Array / easy
Time complexity: O(n log(n)). Space complexity: O(1) - O(n).
"""

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            print(f'nums1[i] = {nums1[i]}, nums2[j] = {nums2[j]}')
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        return res


if __name__ == "__main__":
    numbers1 = [1, 2, 2, 6]
    numbers2 = [9, 2, 7, 2, 4]
    sol = Solution()
    print(sol.intersect(numbers1, numbers2))
