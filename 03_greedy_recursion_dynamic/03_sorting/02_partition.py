'''
Approach 1:
    Sort nums, add min of adjacent pairs.

Approach 2:
    Same as approach 1, but use built in functions

Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # return self.solution_01(nums)
        return self.solution_02(nums)


    def solution_01(self, nums):
        nums = sorted(nums)
        total = 0
        for i in range(0, len(nums), 2):
            total += min(nums[i], nums[i + 1])

        return total


    def solution_02(self, nums):
        nums = sorted(nums)
        return sum( min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2) )


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


    nums = [1,4,3,2]
    t.run(s.arrayPairSum(nums) == 4)

    nums = [1, 2, 3, 4, 5, 6]
    t.run(s.arrayPairSum(nums) == 9)