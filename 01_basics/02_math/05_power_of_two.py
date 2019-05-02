'''
Approach 1:
    Start with 1, increase pow of 2 until reaching num n

Approach 2:
    Start with num, go dow to 1
    All pows of 2 are even => Stop if num becomes odd

Runtime: O(log(n))
Space Complexity: O(1)

Notes: 
    Approach 2 slightly better, on average, stop upon encountering odd number.

'''

from typing import List
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return self.solution_01(n)
        return self.solution_02(n)

    def solution_01(self, n):
        # Edge case: Negative numbers and 0
        if n < 1:
            return False

        power_of_two = self.largest_pow_two(n)
        return n == power_of_two

    def solution_02(self, n):
        # Edge case: Negative numbers and 0
        if n < 1:
            return False

        while n > 1:
            if n % 2 != 0:

                return False

            n //= 2

        return True

    def largest_pow_two(self, n):
        power = 1
        while power < n:
            power *= 2

        return power

# Test
if __name__ == '__main__':
    s = Solution()

    num = 1
    print(s.isPowerOfTwo(num))

    num = 16
    print(s.isPowerOfTwo(num))

    num = 218
    print(s.isPowerOfTwo(num))