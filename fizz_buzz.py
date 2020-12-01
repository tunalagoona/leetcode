"""
Math / easy
O(n) time complexity, O(1) space complexity
"""

from typing import List


class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
        # arr = []
        # k = 1
        # for i in range(0, n):
        #     if k % 3 == 0:
        #         if k % 5 == 0:
        #             arr.append('FizzBuzz')
        #         else:
        #             arr.append('Fizz')
        #     elif k % 5 == 0:
        #         arr.append('Buzz')
        #     else:
        #         arr.append(str(k))
        #     k += 1
        # print(arr)
        # return arr

    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for k in range(1, n + 1):
            ans = ''
            divisible_by_3 = (k % 3 == 0)
            divisible_by_5 = (k % 5 == 0)

            if divisible_by_3:
                ans += "Fuzz"
            if divisible_by_5:
                ans += "Buzz"
            if not divisible_by_3 and not divisible_by_5:
                ans = str(k)
            result.append(ans)
        print(result)
        return result


if __name__ == "__main__":
    num = 17
    s = Solution()
    s.fizzBuzz(num)