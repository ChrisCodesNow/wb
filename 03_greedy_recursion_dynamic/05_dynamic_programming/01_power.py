'''
Approach 1:
    Fill array of sub powers, eventually reaching power x, n
Runtime: O(n)
Space Complexity: O(n)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.solution_01(x, n)


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