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

Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    # ########################################
    # Approach 1
    #
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = self.zero_array(k)
        nums_sum = sum(nums)

        if nums_sum % k != 0:
            return False
        target = nums_sum / k
        start = 0
        return self.partition(nums, subsets, start, target)


    def zero_array(self, size):
        return [0 for _ in range(size)]

    
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
    end = time()
    print(f"Test took {end - start:0.00} seconds")