from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        i = 1
        l = len(nums)
        while True:
            if i == l:
                return l
            if l <= 1:
                return len(nums)
            if nums[i - 1] == nums[i]:
                del nums[i - 1]
                l = len(nums)
            else:
                i += 1
                if i == l:
                    return l


if __name__ == "__main__":
    numbers = [1, 6, 7, 7, 7]
    sol = Solution()
    print(sol.remove_duplicates(numbers))
