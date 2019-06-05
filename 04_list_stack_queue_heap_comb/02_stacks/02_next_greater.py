'''
Approach 1:
    Search right of x for next greater element
Runtime: O(n^2)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.solution_01(nums1, nums2)
        return self.solution_02(nums1, nums2)

    # ########################################
    # Approach 1
    #
    def solution_01(self, nums_1, nums_2):
        if not nums_1 or not nums_2:
            return []

        greater = self.find_next_greater_01(nums_2)
        return [greater[num] for num in nums_1]


    def find_next_greater_01(self, nums):
        greater = dict()
        for i, num in enumerate(nums):
            for next in nums[i + 1 : ]:
                if next > num:
                    greater[num] = next
                    break

            if num not in greater:
                greater[num] = -1

        return greater
            

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
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    t.run(s.nextGreaterElement(nums1, nums2) == [-1,3,-1])

    nums1 = [2,4]
    nums2 = [1,2,3,4]
    t.run(s.nextGreaterElement(nums1, nums2) == [3,-1])