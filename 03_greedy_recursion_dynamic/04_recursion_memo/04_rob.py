'''
Approach 1:
    At each house, get the largest form:
    1. rob house i and houses i + 2 to n - 1
    2. Skip house i and rb houses i + 1 to n - 1

    Base Cases:
        1. Beyond last house: done
        2. At last house, either:
            1. Robbed first house: Stop, don't rob last
            2. Skiped first house: Rob last house
    
    Edge Case:
        Flag if first house was robbed or not

Runtime: O(TBD)
Space Complexity: O(TBD)
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
        return self.rob_r(houses, 0, False)

    
    def rob_r(self, houses, i, rob_first):
        if i >= len(houses):
            return 0
        elif i == len(houses) - 1:
            if rob_first:
                return 0
            else:
                return houses[-1]

        if i == 0:
            return max( houses[i] + self.rob_r(houses, i + 2, True), 
                        self.rob_r(houses, i + 1, False))
        else:
            return max( houses[i] + self.rob_r(houses, i + 2, rob_first),
                        self.rob_r(houses, i + 1, rob_first))


    # ########################################
    # Approach 2
    #
    def solution_02(self, houses):
        memo = dict()
        return self.rob_02(houses, 0, False, memo)


    def rob_02(self, houses, i, rob_first, memo):
        if i >= len(houses):
            return 0
        elif i == len(houses) - 1:
            if rob_first:
                return 0
            else:
                return houses[-1]
        
        elif (i, rob_first) in memo:
            return memo[(i, rob_first)]

        elif i == 0:
            return max(houses[i] + self.rob_02(houses, i + 2, True, memo), 
                    self.rob_02(houses, i + 1, False, memo))
        else:
            memo[(i, rob_first)] =  max(houses[i] + self.rob_02(houses, i + 2, rob_first, memo),
                    self.rob_02(houses, i + 1, rob_first, memo))

            return memo[(i, rob_first)]
                

        
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
