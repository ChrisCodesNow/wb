'''
Approach 1: Bottom up
    Fill array of sub powers, eventually reaching power x, n
Runtime: O(n)
Space Complexity: O(n)

Approach 2: Dynamic Programming
    Solve subproblems bottom, only storing solution to subproblems 
    that will help compute next even and next odd powers.

Runtime: O(n)
Space Complexity: O(1)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return self.solution_01(x, n)
        return self.solution_02(x, n)

    # ########################################
    # Approach 1
    #
    def solution_01(self, x, n):
        negative_pow = n < 0

        n = abs(n)
        powers = [1, x]
        for i in range(2, n + 1):
            if i % 2 == 0:
                powers.append(powers[i // 2] * powers[i // 2])
            else:
                powers.append(powers[i - 1] * x)

        if negative_pow:
            return 1 / powers[n]
        else:
            return powers[n]


    # ########################################
    # Approach 2
    #
    def solution_02(self, x, n):
        is_negative = n < 0
        
        n = abs(n)
        if n == 0:
            return 1
        elif n == 1:
            if is_negative:
                return 1 / x
            else:
                return x

        next_odd = 1           # Help compute next even and odd
        next_even = x
        for i in range(2, n + 1):
            if i % 2 == 0:
                power = next_even * next_even
                next_odd *= x * x
                next_even *= x
            else:
                power = next_odd * x

        if is_negative:
            return 1 / power
        else:
            return power

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