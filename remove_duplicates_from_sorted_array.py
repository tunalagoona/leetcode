from typing import List


class Solution:
    # def remove_duplicates(self, nums: List[int]) -> int:
    #     i = 1
    #     l = len(nums)
    #     while True:  # O(n^2) in the worst case
    #         if i == l:
    #             return l
    #         if l <= 1:
    #             return len(nums)
    #         if nums[i - 1] == nums[i]:
    #             del nums[i - 1]  # O(n)
    #             l = len(nums)
    #         else:
    #             i += 1
    #             if i == l:
    #                 return l

    def remove_duplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        i = 0
        for j in range(1, l):  # O(n^2) in the worst case
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1


if __name__ == "__main__":
    numbers = [1, 6, 7, 7, 7, 8]
    sol = Solution()
    print(sol.remove_duplicates(numbers))
