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