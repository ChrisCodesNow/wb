'''
Approach 1:
    Check mid num, either too high or too low
Runtime: O(logn)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid

        return -1


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


    nums = [-1,0,3,5,9,12]
    target = 9
    t.run(s.search(nums, target) == 4)

    nums = [-1,0,3,5,9,12]
    target = 2
    t.run(s.search(nums, target) == -1)