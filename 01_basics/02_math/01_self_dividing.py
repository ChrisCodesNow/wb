'''

Approach 1: 
    Go through digits, check for 0 and divisibility
Runtime: O(d), for all digits
Space Complexity: O(1)

Approach 2: Use built in functions and generators
    Get digits
    Check for 0's
    Check for divisibility
Runtime: O(d)
Space Complexity: O(d)

Note: Solution 1 is faster
'''

from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        dividing_nums = [ num for num in range(left, right + 1) if self.self_dividing(num) ]

        return dividing_nums

    def self_dividing(self, num):
        return self.solution_01(num)
        # return self.solution_02(num)

    def digits(self, num):
        while num:
            yield num % 10
            num //= 10

    def solution_01(self, num):
        digits = num

        while digits:
            digit = digits % 10
            digits //= 10

            if digit == 0 or num % digit != 0:
                return False

        return True


    def solution_02(self, num):
            if any( digit == 0 for digit in self.digits(num) ):
                return False

            return all( num % digit == 0 for digit in self.digits(num) )
    


# Test
if __name__ == '__main__':
    s = Solution()
    left = 1
    right = 22
    print(s.selfDividingNumbers(left, right) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])