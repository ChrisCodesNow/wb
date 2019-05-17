'''
Approach 1:
    Recursion with memoization
    Base Case: n is 1 => x
    Basae Case: n is 0 => 1
    Even n => x ^(n // 2) * x ^ (n // 2)
    Odd n => x * x ^ (n - 1)

Runtime: O()
Space Complexity: O(logn)
'''
from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = dict()
        if n >= 0:
            return self.pow_r(x, n, memo)
        else:
            return 1 / self.pow_r(x, -n, memo)


    def pow_r(self, x, n, memo):
        if n in memo:
            return memo[n]
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            memo[n] = self.pow_r(x, n // 2, memo) * self.pow_r(x, n // 2, memo)
        else:
            memo[n] = x * self.pow_r(x, n - 1, memo)

        return memo[n]


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


    x = 2.00000
    n = 10
    t.run(s.myPow(x, n) == 1024.00000)

    x = 2.10000
    n = 3
    # Mathematically correct, but rounding issue
    t.run(round(s.myPow(x, n), 5) == round(9.26100, 5)) 

    x = 2.00000
    n = -2
    t.run(s.myPow(x, n) == 0.25000)