from typing import List


class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Insertion sort
    #     """
    #     for k in range(0, n):
    #         nums1[m + k] = nums2[k]
    #     # print(nums1)
    #
    #     for i in range(1, m + n):
    #         key = nums1[i]
    #         j = i - 1
    #         while j >= 0 and key < nums1[j]:
    #             nums1[j + 1] = nums1[j]
    #             j -= 1
    #         nums1[j + 1] = key
    #     # print(nums1)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


if __name__ == "__main__":
    s = Solution()

    numbers1 = [1, 2, 3, 0, 0, 0]
    nums1_len = 3
    numbers2 = [2, 5, 6]
    nums2_len = 3

    s.merge(numbers1, nums1_len, numbers2, nums2_len)
