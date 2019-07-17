'''
Approach 1:
    n = size of array
    Q = Queue with first k numbers in nums

    Iterate nums from [k to n - 1]:
        Save num at index i to Q
        nums[i] = next num in Q
    
    Iterate nums from [0 to k - 1]:
        nums[i] = next num in Q

Runtime: O(n)
Space Complexity: O(k)


Approach 2:
    Iterate k times:
        Move current last num to front of nums list

    Move front:
        new_front = last num in nums list
        Iterate [n - 1 to 0]:
            nums[i] = prev num, that is nums[i - 1]

        Front num = new_front, that is nums[0] = new_front
Runtime: O(kn)
Space Complexity: O(k)


Approach 3: Similar to approach 2, but use python3 array built in methods
    Iterate k times:
        Move current last num to front of nums list

Runtime: O(kn)
Space Complexity: O(k)
'''
from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.solution_01(nums, k)
        # self.solution_02(nums, k)
        self.solution_03(nums, k)

    # ########################################
    # Approach 1
    #
    def solution_01(self, nums, k):
        if not nums or k == 0:
            return

        n = len(nums)
        k = k % n
        Q = deque(nums[:k])

        for i in range(k, n):
            Q.append(nums[i])
            nums[i] = Q.popleft()

        for i in range(k):
            nums[i] = Q.popleft()


    # ########################################
    # Approach 2
    #
    def solution_02(self, nums, k):
        if not nums or k == 0:
            return
        
        n = len(nums)
        k = k % n
        for _ in range(k):
            self.move_last_to_front(nums)
        

    # Moves the last element to the front of the list
    def move_last_to_front(self, nums):
        new_front = nums[-1]
        n = len(nums)
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        
        nums[0] = new_front


    # ########################################
    # Approach 3
    #
    def solution_03(self, nums, k):
        if not nums or k == 0:
            return
        
        n = len(nums)
        k = k % n
        for _ in range(k):
            new_front = nums.pop()
            nums.insert(0, new_front)


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


    nums = [1,2,3,4,5,6,7]
    k = 3
    result = [5,6,7,1,2,3,4]
    solution.rotate(nums, k)
    my_result = nums
    test.run(result == my_result)

    nums = [-1,-100,3,99]
    k = 2
    result = [3,99,-1,-100]
    solution.rotate(nums, k)
    my_result = nums
    test.run(result == my_result)