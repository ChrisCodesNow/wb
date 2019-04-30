'''
Approach 1: 
    Create matrix T with m rows.
    Fill T from A's old col to T's new row

Runtime: O(nm)
Space Complexity: O(nm)
'''

# Asume input matrix is a 2D
from typing import List
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        T = [ [] for _ in range(len(A[0])) ]

        for row in A:
            for j,ele in enumerate(row):
                T[j].append(ele)

        return T


# Test
if __name__ == '__main__':
    s = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.transpose(A))
    
    A = [[1,2,3],[4,5,6]]
    print(s.transpose(A))
    
    # Error: Method expects 2D matrix
    # A = [1, 2, 3, 4]
    # print(s.transpose(A))