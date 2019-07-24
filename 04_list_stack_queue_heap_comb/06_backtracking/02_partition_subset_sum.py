'''
Approach 1:
    target = num to add to
    candidates = list of given nums
    selected = list of chosen nums from candidate list
    total = sum of current selected nums
    start = index of where to start looking
            (Avoids duplicate selects s.a.: [2, 2, 3], and [3, 2, 2], etc)
    n = size of candidates list

    comb_sum(candidates, target, selected, total, start):
        Base:
            total = target:
                => save current selected
        Iterate candidates on index i [start, n - 1]:
            total + candidates[i] <= target:
                Add candidates[i] to selected
                Recursively comb sum at start = i + 1:
                    Do any of the recursive subproblems get eq subset sum?:
                        => True
                Remove candidates[i] from selected

            No eq subset sum found at curr subproblem:
                => False
                
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return self.solution_01(nums)
        return self.solution_02(nums)
        
    # ########################################
    # Approach 1
    #
    def solution_01(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        
        target = nums_sum / 2
        return self.equal_subset_sum(nums, target, 0, 0)


    def equal_subset_sum(self, nums, target, total, start):
        if total == target:
            return True

        for i in range(start, len(nums)):
            if total + nums[i] <= target:
                if self.equal_subset_sum(nums, target, total + nums[i], i + 1):
                    return True

        return False


    # ########################################
    # Approach 2
    #
    def solution_02(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
            
        target = sum(nums) / 2
        memo = dict()
        return self.eqsum(nums, target, 0, 0, memo)


    def eqsum(self, nums, target, total, start, memo):
        if (start, total) in memo:
            return memo[start, total]
        elif total == target:
            return True
        elif start > len(nums) - 1:
            return False
        
        for i in range(start, len(nums)):
            if total + nums[i] <= target:
                if self.eqsum(nums, target, total + nums[i], i + 1, memo):
                    memo[start, total] = True
                    return memo[start, total]
        
        memo[start, total] = False
        return memo[start, total]
        


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
    solution = Solution()
    test = Test()

    nums = [1, 5, 11, 5]
    result = True
    my_result = solution.canPartition(nums)
    test.run(result == my_result)

    nums = [1, 2, 3, 5]
    result = False
    my_result = solution.canPartition(nums)
    test.run(result == my_result)

    nums = [99,2,3,98]
    result = True
    my_result = solution.canPartition(nums)
    test.run(result == my_result)

    nums = [17,58,41,75,61,70,52,7,38,11,40,58,44,45,4,81,67,54,79,80,15,3,14,16,9,66,69,41,72,37,28,3,33,90,56,12,72,49,35,22,49,27,49,82,41,77,100,82,18,95,24,51,37,2,34,82,70,53,73,32,90,98,81,22,73,76,79,40,27,62,45,96,36,15,63,28,54,88,63,37,58,9,62,98,93,72,99,53,91,29,61,31,11,42,20,35,50,68,10,86]
    result = False
    my_result = solution.canPartition(nums)
    test.run(result == my_result)


    nums = [
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,100
    ]
    result = False
    my_result = solution.canPartition(nums)
    test.run(result == my_result)


    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
    result = False
    my_result = solution.canPartition(nums)
    test.run(result == my_result)


    nums = [
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,97,95
    ]
    result = True
    my_result = solution.canPartition(nums)
    test.run(result == my_result)
