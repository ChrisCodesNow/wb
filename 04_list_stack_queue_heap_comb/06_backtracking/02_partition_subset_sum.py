'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
    # Approach 1
    #

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
    result = True
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
