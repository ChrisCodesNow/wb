'''
Approach 1:
    Remove duplicates, get intersection
Runtime: O(m)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniq_1 = set(nums1)
        uniq_2 = set(nums2)

        return list(uniq_1 & uniq_2)


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


    nums1 = [1,2,2,1]
    nums2 = [2,2]
    t.run(s.intersection(nums1, nums2) == [2])

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    t.run(s.intersection(nums1, nums2) == [9,4])

    nums1 = []
    nums2 = [9,4,9,8,4]
    t.run(s.intersection(nums1, nums2) == [])

    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    t.run(s.intersection(nums1, nums2) == [1, 2, 3])