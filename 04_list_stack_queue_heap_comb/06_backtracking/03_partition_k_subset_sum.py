'''
Approach 1:
    n = size of nums
    subsets = zero array of size k
    sum of nums not divisible by k:
        => No valid partition exists => F
    
    target = sum of nums / k
    start = 0
    Get result of partition(nums, k, subsets, start, target)

    partition(nums, k, subsets, start, target):
        Base 1:
            Have k groups where each sum = target:
                => Valid partition found => T
        Base 2:
            No more nums remaining:
                => F
        Iterate nums i [start, n - 1]:
            Iterate subset groups j [0, k - 1]:
                subet[j] + nums[i] <= target:
                    Add nums[i] to subset[k]
                    Recursively serach for partition with (start = i + 1):
                        Partition found => T
                    Remove nums[i] from subset[k]
        No valid partition found:
            => F


Approach 2: Similar to approach 1, but use memoization
    n = size of nums
    k = number of desired subsets
    subsets = zero array of size k
    sum of nums not divisible by k:
        => No valid parititon exists => F

    target = sum of nums / k
    start = 0
    Get result of partition(nums, target, subsets, start, memo)

    partition(nums, target, subsets, start, memo):
        subsets_tup = subsets represented as a tuple
        Base 1: 
            (start, subsets_tup) already in memo:
                => Get memo[start, subsets_tup]
        Base 2:
            All k subsets have sum of target:
                => Found k valid partitions => True
        Base 3:
            start >= n:
                => Did not find k valid partitions => False

        Iterate nums i [start, n - 1]:
            Iterate subsets j [0 to k - 1]:
                nums[i] + subsets[j] <= target:
                    Add nums[i] to subset[j]
                    Recursively partition with start = i + 1
                    Save recursive partition result to memo[start, subsets_tup]
                    If recursive partition finds solution:
                        => True
                    Remove nums[i] from subset[j]
        
        No valid partitions found with current combinations:
            => False

Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # return self.solution_01(nums, k)
        return self.solution_02(nums, k)


    # ########################################
    # Approach 1
    #
    def solution_01(self, nums, k):
        nums_sum = sum(nums)

        if nums_sum % k != 0:
            return False
        target = nums_sum / k
        start = 0
        subsets = self.zero_array(k)
        return self.partition(nums, subsets, start, target)

    
    def partition(self, nums, subsets, start, target):
        if all(s == target for s in subsets):
            return True
        elif start >= len(nums):
            return False
        
        for i in range(len(nums)):
            for j in range(len(subsets)):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if self.partition(nums, subsets, i + 1, target):
                        return True
                    subsets[j] -= nums[i]

        return False

    # ########################################
    # Approach 2
    #
    def solution_02(self, nums, k):
        nums_sum = sum(nums)

        if nums_sum % k != 0:
            return False
        target = nums_sum / k
        start = 0
        subsets = self.zero_array(k)
        memo = dict()

        return self.partition_02(nums, target, subsets, start, memo)


    def zero_array(self, size):
        return [0 for _ in range(size)]


    def partition_02(self, nums, target, subsets, start, memo):
        subsets_tup = tuple(subsets)
        if (start, subsets_tup) in memo:
            return memo[start, subsets_tup]
        elif all(subset == target for subset in subsets):
            return True
        elif start >= len(nums):
            return False

        for i in range(start, len(nums)):
            for j in range(len(subsets)):
                if nums[i] + subsets[j] <= target:
                    subsets[j] += nums[i]
                    if self.partition_02(nums, target, subsets, i + 1, memo):
                        return True
                    subsets[j] -= nums[i]

        memo[start, subsets_tup] = False
        return False


# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
from time import time
if __name__ == '__main__':
    solution = Solution()
    test = Test()


    start = time()

    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    result = True
    my_result = solution.canPartitionKSubsets(nums, k)
    test.run(result == my_result)


    nums = [2,2,10,5,2,7,2,2,13]
    k = 3
    result = True
    my_result = solution.canPartitionKSubsets(nums, k)
    test.run(result == my_result)

    nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
    k = 5
    result = True
    my_result = solution.canPartitionKSubsets(nums, k)
    test.run(result == my_result)

    
    end = time()
    print(f"Test took {end - start:0.00} seconds")