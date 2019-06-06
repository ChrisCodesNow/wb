'''
Approach 1:
    Base: 
        Permutation of empty list => Empty set
    Recursive:
        Get permutations of A 0 to n - 2
        Place current char A n - 1 in between each slot of each prev subset
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        else:
            curr_val = nums[-1]
            prev_permutations = self.permute(nums[:-1])
            curr_permutations = []
            for prev_perm in prev_permutations:
                for i in range(len(prev_perm) + 1):
                    curr_permutations.append(prev_perm[:i] + [curr_val] + prev_perm[i:])

            return curr_permutations


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
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    output = s.permute(nums)
    t.run(sorted(answer) == sorted(output))