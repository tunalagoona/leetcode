"""
https://leetcode.com/problems/count-primes/
"""


# time complexity: O(n Log log n)
# space complexity: O(n)
class Solution:
    def count_primes(self, n: int) -> int:
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

        return count
