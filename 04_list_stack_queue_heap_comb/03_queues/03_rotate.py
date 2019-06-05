'''
Approach 1:
    Save last k eleements.
    Replace and save each array element with Q's.
Runtime: O()
Space Complexity: O()
'''
from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Q = deque(nums[-k:])
        for i,num in enumerate(nums):
            Q.append(num)
            nums[i] = Q.popleft()

        return nums


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

    nums= [1,2,3,4,5,6,7] 
    k = 3
    s.rotate(nums, k)
    t.run(nums == [5,6,7,1,2,3,4])

    nums= [-1,-100,3,99] 
    k = 2
    s.rotate(nums, k)
    t.run(nums == [3,99,-1,-100])