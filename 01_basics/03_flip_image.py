"""
Approach 1: 
    In place modify 2D matrix
    Flip each row, then reverse each bit

Approach 2:
    Same concept as 1, but use map() instead of iteration

Runtime: O(nm)
Space Complexity: O(m), when dealing with rows of length O(m)
"""

from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return self.solution_01(A)
        # return self.solution_02(A)


    def solution_01(self, A):
        for i in range(len(A)):
            A[i] = self.flip_h(A[i])
            for j in range(len(A[i])):
                A[i][j] = self.invert(A[i][j])

        return A


    def solution_02(self, A):
        A = list(map(self.flip_h, A))
        for i in range(len(A)):
            A[i] = list(map(self.invert, A[i]))

        return A


    # Flips row
    def flip_h(self, A):
        return A[::-1]


    # Apply inverse on each bit
    def invert(self, bit):
        if bit == 1:
            return 0
        else:
            return 1

# Test
if __name__ == '__main__':
    s = Solution()

    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage(A) == [[1,0,0],[0,1,0],[1,1,1]])

    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(s.flipAndInvertImage(A) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])