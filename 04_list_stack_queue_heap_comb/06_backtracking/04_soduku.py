'''
Approach 1:
    board = sodoku of size 9 x 9
    n = size of board = 0
    rows = array with n sets
    cols = array with n sets
    squares = array with n sets

    Mark used inintializer(rows, cols, squares):
        At each row i of board:
            Add every used num to set at rows[i]
        At each col j of board:
            Add every used num to set at cols[j]
        At each square k of board:
            Add every used num to set at cols[k]


    row = 0, col = 0
    Solve(board, rows, cols, squares, row, col):
        Base 1:
            At end of board (rows and columns wise)
            =>  Found solution => True
        
        Iterate rows i [row, n - 1]:
            Iterate cols j [col, n - 1]:
                idx = i, j
                board @ idx not chose:
                    Iterate num candidates [1, n = 9]:
                        place num in board @ idx
                        mark num as placed in rows, cols, squares
                        nex position =  {row, col + 1 if col < n - 1
                                        {row + 1, col otherwise (at end of col)
                        Recursevly solve at next position
                        If solved recursively:
                            => True
                        Unmark num from placed in rows, cols, squares
                        Remove num from board @ idx

        Can't solve current board:
            => False


Helper methods:
    idx chosen(board, idx):
        Does board @ idx = '.'  ?
    
    disrupt(rows, cols, squares, idx, candidate):
        i, j = idx
        Is candidate already in:
            rows[i], cols[j], or squares[square_idx(idx)] ?
    
    square_idx(idx):
        i, j = idx
        row = i // 3
        col = j // 3
        total = 3 * row + col

    mark place(board, rows, cols, squares, num, idx):
        i, j = idx
        board @ idx = num
        Add num to set at:
            rows[i], cols[j], squares[square_idx(idx)]

    unmark_remove(board, rows, cols, squares, num, idx):
        i, j = idx
        Make board @ idx empty => board @ idx = '.'
        Remove num from set at:
            rows[i], cols[j], squares[square_idx(idx)]

Runtime: O()
Space Complexity: O()
'''
from typing import List

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