'''
Approach 1:
    Get inland zeros in a set
    Get border zeros

    BFS on each border zero:
        Remove adjacent zeros from inland zeros
        Only add adjacent zeros to Q

    Convert remaining inland zeros to 'X'

Runtime: O(mn)
Space Complexity: O(mn)
'''
from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board:
            inland_zeros = self.get_inland_zeros(board)
            border_zeros = self.get_border_zeros(board)

            self.bfs(board, border_zeros, inland_zeros)

            self.surround_regions(board, inland_zeros)


    # ########################################
    # Approach 1
    #
    def get_inland_zeros(self, board):
        zeros = set()
        m,n = len(board), len(board[0])

        for i in range(1, m - 1):
            for j in range(1, n -1):
                if board[i][j] == 'O':
                    zeros.add((i,j))

        return zeros


    def get_border_zeros(self, board):
        return self.top_zeros(board) + \
                self.bottom_zeros(board) + \
                self.left_zeros(board) + \
                self.right_zeros(board)

    
    def top_zeros(self, board):
        n = len(board[0])
        return [(0, j) for j in range(n) if board[0][j] == 'O']

    
    def bottom_zeros(self, board):
        m,n = len(board), len(board[-1])
        return [(m - 1, j) for j in range(n) if board[-1][j] == 'O']


    def left_zeros(self, board):
        m = len(board)
        return [(i, 0) for i in range(1, m - 1) if board[i][0] == 'O']


    def right_zeros(self, board):
        m,n = len(board), len(board[0])
        return [(i, n - 1) for i in range(1, m - 1) if board[i][-1] == 'O']


    def bfs(self, board, border_zeros, inland_zeros):
        visited = set()
        Q = deque(border_zeros)
        while Q:
            u = Q.popleft()
            visited.add(u)

            for v in self.neighbors(board, u):
                if v not in visited:
                    i,j = v
                    if board[i][j] == 'O':
                        if v in inland_zeros:
                            inland_zeros.remove(v)
                        Q.append(v)


    def surround_regions(self, board, inland_zeros):
        for i,j in inland_zeros:
            board[i][j] = 'X'


    def neighbors(self, board, u):
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
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    new_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    s.solve(board)
    t.run(board == new_board)


    board = [
        ["O","O"],
        ["O","O"]
    ]
    new_board = [
        ["O","O"],
        ["O","O"]
    ]
    s.solve(board)
    t.run(board == new_board)

    