'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        lip = 0
        memo = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lip = max(lip, self.DFS(matrix, (i,j), memo))

        return lip

    
    def DFS(self, matrix, src, memo):
        if src in memo:
            return memo[src]
        
        i,j = src
        memo[src] = 1
        for v in self.neighbors(matrix, src):
            v_i, v_j = v
            if matrix[v_i][v_j] > matrix[i][j]:
                memo[src] = max(memo[src], 1 + self.DFS(matrix, v, memo))
        
        return memo[src]


    def neighbors(self, matrix, src):
        m,n = len(matrix), len(matrix[0])
        i,j = src
        if i - 1 >= 0:
            yield (i - 1, j)
        if i + 1 < m:
            yield (i + 1, j)
        if j - 1 >= 0:
            yield (i, j - 1)
        if j + 1 < n:
            yield (i, j + 1)

    # ########################################
    # Approach 1
    #

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


    nums = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
    ] 
    result = 4 
    my_result = solution.longestIncreasingPath(nums)
    test.run(my_result == result)

    nums = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
    ] 
    result = 4 
    my_result = solution.longestIncreasingPath(nums)
    test.run(my_result == result)