'''
Approach 1:
    Base: 
        Susets of empty list => empty set
    Recursive:
        Get prev subsets A 0 to n-2
        Add curr char A n-1 at end of each prev subset
        
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            char = nums[-1]
            prev_subsets = self.subsets(nums[:-1])
            curr_subsets = []
            for prev_sub in prev_subsets:
                curr_subsets.append(prev_sub + [char])

            return prev_subsets + curr_subsets


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
        
    nums = [1,2,3]
    answer = [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    output = s.subsets(nums)
    t.run(sorted(answer) == sorted(output))