'''
Approach 1:
    Use xor associativity and property of removing pair duplicate
Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor


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

    nums = [2,2,1]
    t.run(s.singleNumber(nums) == 1)

    nums = [4,1,2,1,2]
    t.run(s.singleNumber(nums) == 4)

    nums = [4,1,1]
    t.run(s.singleNumber(nums) == 4)


    