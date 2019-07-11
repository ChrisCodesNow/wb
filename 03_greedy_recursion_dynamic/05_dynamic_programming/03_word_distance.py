'''
Approach 1:
    m = size of word 1
    n = size of word 2
    Create grid of size (m + 1) X (n + 1)
    Fill grid with 0's
    Fill last row with values (n to 0)
    Fill last column with values (m to 0)

    Compute edit distance:
        Iterate rows m - 1 to 0:
            Iterate columns n - 1 to 0:
                insert cost = grid[i, j + 1]
                delete cost = grid[i + 1, j]
                replace cost = grid[i + 1, j + 1]

                word1[i] = word2[j]:
                    grid[i,j] = replace cost
                Otherwise:
                    grid[i,j] = min(insert, replace, delete) + 1

        Minimum distance from word1 to word2 = grid[0, 0]

Runtime: O(m * n)
Space Complexity: O(m * n)
'''
from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.solution_01(word1, word2)


    # ########################################
    # Approach 1
    #
    def solution_01(self, word_1, word_2):
        m = len(word_1)
        n = len(word_2)

        grid = self.make_zero_board(m + 1, n + 1)
        self.fill_last_row(grid, n)
        self.fill_last_col(grid, m)
        min_distance = self.compute_distance(grid, word_1, word_2)
        
        return min_distance


    def make_zero_board(self, rows, cols):
        return [[0 for _ in range(cols)] for __ in range(rows)]

    
    def fill_last_row(self, grid, row_val):
        for j in range(len(grid[-1])):
            grid[-1][j] = row_val
            row_val -= 1

    
    def fill_last_col(self, grid, col_val):
        for i in range(len(grid)):
            grid[i][-1] = col_val
            col_val -= 1


    def compute_distance(self, grid, word_1, word_2):
        rows = len(word_1) - 1
        cols = len(word_2) - 1
        
        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                insert = grid[i][j + 1]
                delete = grid[i + 1][j]
                replace = grid[i + 1][j + 1]

                if word_1[i] == word_2[j]:
                    grid[i][j] = replace
                else:
                    grid[i][j] = min(insert, delete, replace) + 1


        return grid[0][0]


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

    word1 = "horse"
    word2 = "ros"
    result = 3
    my_result = solution.minDistance(word1, word2)
    test.run(my_result == result)
    

    word1 = "intention"
    word2 = "execution"
    result = 5
    my_result = solution.minDistance(word1, word2)
    test.run(my_result == result)