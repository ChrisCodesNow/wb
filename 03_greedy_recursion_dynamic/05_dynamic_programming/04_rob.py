'''
Approach 1:
    Bottom up, starting with base cases, fill array with results of subproblems, 
    eventually solving original problem

    At each house i, either:
    1. Rob house i and houses i + 2 to n - 1
    2. Rob houses i + 1 to n - 1

Runtime: O(n)
Space Complexity: O(n)

Approach 2:
    Dynamic Programming, similar to approach 1, but only save results of 
    subproblems i + 1 and i + 2.

Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # return self.solution_01(nums)
        return self.solution_02(nums)


    # ########################################
    # Approach 1
    #
    def solution_01(self, houses):
        n = len(houses)
        if n < 2:
            return 0

        rob_first = [0] * n
        skip_first = houses[:]

        rob_first[-2] = max(houses[-2], rob_first[-1])
        skip_first[-2] = max(houses[-2], skip_first[-1])

        for i in range(n - 3, -1, -1):
            rob_first[i] = max(houses[i] + rob_first[i + 2], rob_first[i + 1])
            skip_first[i] = max(houses[i] + skip_first[i + 2], skip_first[i + 1])

        return max(rob_first[0], skip_first[i + 1])



    # ########################################
    # Approach 2
    #
    def solution_02(self, houses):
        n = len(houses)
        if n < 2:
            return 0

        rob_first = [0] * 3
        skip_first = houses[-3:]

        rob_first[-2] = max(houses[-2], rob_first[-1])
        skip_first[-2] = max(houses[-2], skip_first[-1])

        for i in range(n - 3, -1, -1):
            rob_first[0] = max(houses[i] + rob_first[2], rob_first[1])
            rob_first[-1] = rob_first[-2]
            rob_first[-2] = rob_first[-3]

            if i > 0:
                skip_first[0] = max(houses[i] + skip_first[2], skip_first[1])
                skip_first[-1] = skip_first[-2]
                skip_first[-2] = skip_first[-3]

        return max(rob_first[0], skip_first[0])

# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
import time
if __name__ == '__main__':
    s = Solution()
    t = Test()

    start = time.time()
    nums = [2,3,2]
    t.run(s.rob(nums) == 3)

    nums = [1,2,3,1]
    t.run(s.rob(nums) == 4)
    end = time.time()
    print(f'Elapsed time = {(end-start)}')



    start = time.time()
    nums = [94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]
    # time exceeded error
    t.run(s.rob(nums) == 2926)
    end = time.time()
    print(f'Elapsed time = {(end-start)}')