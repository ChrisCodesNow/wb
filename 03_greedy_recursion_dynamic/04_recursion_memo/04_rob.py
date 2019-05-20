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
        return self.solution_01(nums)


    def solution_01(self, nums):
        return self.rob_r(nums, 0, False)

    
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

    nums = [2,3,2]
    t.run(s.rob(nums) == 3)

    nums = [1,2,3,1]
    t.run(s.rob(nums) == 4)