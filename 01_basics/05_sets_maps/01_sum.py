'''
Approach 1:
    Get num's comp, or mark num as seen

Approach 2:
    Save num->idx in hash table, get num's comp from hash table (distinct idx)

Runtime: O(n)
Space Complexity: O(n)

Notes:
    Approach 1 stops as soon as it finds distinct indexed complement
'''
from typing import List
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.solution_01(nums, target)
        return self.solution_02(nums, target)

    def solution_01(self, nums, target):
        seen_nums_idx = dict()
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen_nums_idx:
                return [seen_nums_idx[complement], i]
            else:
                seen_nums_idx[num] = i


    def solution_02(self, nums, target):
        nums_idx = self.get_nums_idx(nums)
        for i,num in enumerate(nums):
            complement = target - num
            
            if complement in nums_idx:
                # Avoid same num at same idx
                if not (num == complement and len(nums_idx[complement]) == 1):
                    return self.get_complement_idx(nums_idx, complement, i)


    def get_nums_idx(self, nums):
        nums_idx = defaultdict(set)
        for i,num in enumerate(nums):
            nums_idx[num].add(i)

        return nums_idx

    def get_complement_idx(self, nums_idx, complement, num_idx):
        for idx in nums_idx[complement]:
            if idx != num_idx:      # Avoid same indices    ## Bugfix: Remove this line(look line 33)
                return [num_idx, idx]

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


    nums = [2, 7, 11, 15]
    target = 9
    t.run(s.twoSum(nums, target) == [0, 1])


    nums = [3,2,4]
    target = 6
    t.run(s.twoSum(nums, target) == [1, 2])
    # Output
    # null
    # Expected
    # [1,2]