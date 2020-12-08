"""
Math / easy
Time complexity: O(n log log n). Space complexity: O(n).
"""
# from math import sqrt


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         count = 0
#         for i in range(1, n):
#             if self.is_prime(i):
#                 count += 1
#
#         print(count)
#         return count
#
#     def is_prime(self, num: int) -> bool:
#         if num <= 1:
#             return False
#         for i in range(2, int(sqrt(num)) + 1):
#             if num % i == 0:
#                 return False
#         return True


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [False, False]
        for i in range(2, n):
            is_prime.append(True)

        j = 2
        while j * j < n:
            if not is_prime[j]:
                continue
            for k in range(j * j, n, j):
                is_prime[k] = False
            j += 1

        count = 0
        for i in range(0, n):
            if is_prime[i]:
                count += 1
        print(count)
        return count


if __name__ == "__main__":
    number = 4
    sol = Solution()
    sol.countPrimes(number)
