'''
Approach 1:
    Get character count, find duplicate and missing numbers

Runtime: O(nlogn)
Space Complexity: O(n)

Approach 2:
    Similar to approach 1, but don't sort
Runtime: O(nlogn)
Space Complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # return self.solution_01(nums)
        return self.solution_02(nums)


    def solution_01(self, nums):
        duplicate, num_count = self.get_duplicate(nums)
        missing = self.get_missing(nums, num_count)
        return [duplicate, missing]


    def solution_02(self, nums):
        num_count = Counter(nums)

        for num in range(1, len(nums) + 1):
            if num_count[num] == 2:
                duplicate = num

            if num not in num_count:
                missing = num

        return [duplicate, missing]


    def get_duplicate(self, nums):
        num_count = Counter(nums)
        duplicate = num_count.most_common(1)[0][0]
        num_count[duplicate] -= 1

        return duplicate, num_count


    def get_missing(self, nums, num_count):
        correct = Counter(range(1, len(nums) + 1))
        missing = correct - num_count
        missing = missing.most_common(1)[0][0]

        return missing


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

    nums = [1,2,2,4] 
    t.run(s.findErrorNums(nums) == [2,3])

    nums = [1,1]
    t.run(s.findErrorNums(nums) == [1, 2])