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

        divider = 2
        while divider * divider < n:
            if is_prime[divider]:
                for num in range(divider * divider, n, divider):
                    is_prime[num] = False
            divider += 1

        count = 0
        for num in is_prime:
            if num:
                count += 1

        print(count)
        return count


if __name__ == "__main__":
    number = 38
    sol = Solution()
    sol.countPrimes(number)
