'''
Approach 1:
    Get digits, add squared digits.
    Eigher endless loop or reach a 1

Runtime: O(cycle or 1)
Space Complexity: O(cycle or 1)
'''
from typing import List
class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        while True:
            if n in seen_nums:
                return False
            if n == 1:
                return True

            seen_nums.add(n)
            n = self.sum_squared_digits(n)

    
    # Add square of each digit
    def sum_squared_digits(self, num):
        digits = self.get_digits(num)
        squared_digits = [digit * digit for digit in digits]
        return sum(squared_digits)


    # LSB in front
    def get_digits(self, num):
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10

        return digits


# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
if __name__ == '__main__':
    s = Solution()
    t = Test()

    num = 19
    t.run(s.isHappy(num) == True)

    num = 20
    t.run(s.isHappy(num) == False)