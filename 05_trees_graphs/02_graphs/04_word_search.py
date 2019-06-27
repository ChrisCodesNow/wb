'''
Approach 1:
    Modified BFS
    Get start location of 1st letter in grid.
    DFS on each start location:
        current char on board == char search:
            Continue BFS on next char of word
            Any of paths build entire word?

    Else: False

Runtime: O(m*n)
Space Complexity: O(m*n)
'''
from collections import deque
from typing import List
class Solution:
    # ########################################
    # Approach 1
    #
    def exist(self, board: List[List[str]], word: str) -> bool:
        locations = self.get_locations(board, word[0])
        for location in locations:
            if self.can_build_word(board, word, location):
                return True

        return False


    def can_build_word(self, board, word, location):
        visited = set()
        Q = deque([(location, 0)])
        while Q:
            u, idx = Q.popleft()
            i,j = u
            if board[i][j] == word[idx]:
                visited.add(u)
                if idx == len(word) - 1:
                    return True
                else:
                    for v in self.get_neighbors(board, u):
                        if v not in visited:
                            Q.append((v, idx + 1))
        return False


    def get_locations(self, board, char):
        locations = []
        for i,row in enumerate(board):
            for j,value in enumerate(row):
                if char == value:
                    locations.append((i,j))
        
        return locations

    
    def get_neighbors(self, board, u):
        i,j = u
        m,n = len(board), len(board[0])

        if i - 1 >= 0:
            yield (i - 1, j)
        if i + 1 < m:
            yield (i + 1, j)
        if j - 1 >= 0:
            yield (i, j - 1)
        if j + 1 < n:
            yield (i, j + 1)


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

    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    word = "ABCCED"
    t.run(s.exist(board, word) == True)

    word = "SEE"
    t.run(s.exist(board, word) == True)

    word = "ABCB"
    t.run(s.exist(board, word) == False)


    board = [
        ["a","a"]
    ]
    word = "aaa"
    t.run(s.exist(board, word) == False)


    board = [
        ["a","b"],
        ["c","d"]
    ]
    word = "acdb"
    t.run(s.exist(board, word) == True)