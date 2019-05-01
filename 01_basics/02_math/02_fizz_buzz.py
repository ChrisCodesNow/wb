'''
Approach 1: Do it all in same code
    Go through range, and determine fibuzz string at each value.

Approach 2:
    Same as approach 1, but refactor code into components

Runtime: O(n)
Space Complexity: O(n), list of size n

Note: Approach 01 had better result
'''
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # return self.solution_01(n)
        return self.solution_02(n)

    def solution_01(self, n):
        fb_list = []

        for num in range(1, n + 1):
            if num % 5 == 0 and num % 3 == 0:
                fb_list.append('FizzBuzz')
            elif num % 3 == 0:
                fb_list.append('Fizz')
            elif num % 5 == 0:
                fb_list.append('Buzz')
            else:
                fb_list.append(str(num))

        return fb_list

    def solution_02(self, n):
        # fb_list = [ self.fb_str(num) for num in range(1, n + 1) ]
        fb_list = list(map(self.fb_str, range(1, n + 1)))
        return fb_list

    # Return fizzbuzz string of the input number
    def fb_str(self, num):
        if self.is_factor(num, 3) and self.is_factor(num, 5):
            return 'FizzBuzz'
        if self.is_factor(num, 3):
            return 'Fizz'
        if self.is_factor(num, 5):
            return 'Buzz'
        else:
            return str(num)

    # Return True if m is factor of n
    def is_factor(self, n, m):
        return n % m == 0
        
# Test
if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15) == [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
])