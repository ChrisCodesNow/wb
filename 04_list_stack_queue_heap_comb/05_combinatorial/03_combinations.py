'''
Approach 1:
    Base: 
        Empty set => Empty Set.
        k = 1 => Get each element
    Recursive:
        Pick and remove current list element.
        Get combinations of remaining list elements, chooking k-1.
        Combine chose element with each of previous combinations

Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        A = list(range(1, n + 1))
        return self.combinations(A, k)


    def combinations(self, A, k):
        if not A:
            return []
        elif k == 1:
            return [[ele] for ele in A]

        else:
            curr_combs = []
            for i, ele in enumerate(A):
                prev_combs = self.combinations(A[i + 1:], k - 1)
                for prev_comb in prev_combs:
                    curr_combs.append([ele] + prev_comb)

            return curr_combs


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


    n = 4
    k = 2
    answer = [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    output = s.combine(n, k)
    t.run(sorted(answer) == sorted(output))