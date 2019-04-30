'''
Approach 1: One pass, get evens and odds, then join
Runtime: O(n)
Space Complexity: O(n)


Approach 2: In place, use pivot to separate evens and odds
Runtime: O(n)
Space Complexity: O(1)


Approach :
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:

    # Evens followed by odds
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # return self.solution_01(A)
        return self.solution_02(A)

    def solution_01(self, A):
        evens = [ num for num in A if num % 2 == 0 ]
        odds = [ num for num in A if num % 2 != 0 ]

        return evens + odds

    def solution_02(self, A):
        pivot = 0
        for i in range(len(A)):
            # Push evens inside pivot
            if A[i] % 2 == 0:
                A[i], A[pivot] = A[pivot], A[i]
                pivot += 1

        return A

def main():
    s = Solution()
    l1 = [3,1,2,4]
    print(s.sortArrayByParity(l1))
    
if __name__ == '__main__':
    main()
