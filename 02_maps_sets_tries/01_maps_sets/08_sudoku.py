'''
Approach 1:
    Validate rows, cols, and 3x3 boxes

Runtime: O(mn)
Space Complexity: O(mn)
'''
from typing import List
class Solution:
    # 2D List str -> Bool
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self.valid_rows(board))
        print(self.valid_cols(board))
        print(self.valid_boxes(board))

        return self.valid_rows(board) and \
                self.valid_cols(board) and \
                self.valid_boxes(board)


    # 2D List str -> Bool
    def valid_rows(self, board):
        for row in board:
            if not self.valid_row(row):
                return False

        return True


    # List str -> Bool
    def valid_row(self, row):
        return self.has_unique_nums(row)


    # 2D List str -> Bool
    def valid_cols(self, board):
        cols = self.get_cols(board)
        for col in cols:
            if not self.valid_col(col):
                return False
        
        return True


    # 2D List str -> Yielded 2D List Str
    def get_cols(self, board):
        for j in range(len(board[0])):
            col = [board[i][j] for i in range(len(board))]
            yield col


    # List str -> Bool
    def valid_col(self, col):
        return self.has_unique_nums(col)


    # 2D List str -> Bool
    def valid_boxes(self, board):
        boxes = self.get_boxes(board)
        for box in boxes:
            if not self.valid_box(box):
                return False

        return True


    # 2D List str -> 2D List str
    def get_boxes(self, board):
        left = []
        mid = []
        right = []

        for i,row in enumerate(board):
            if i % 3 == 0 and i != 0:
                yield left
                yield mid
                yield right

                left = []
                mid = []
                right = []

            left = left + row[:3]
            mid = mid + row[3:6]
            right = right + row[6:]

        # Yield last one
        yield left
        yield mid
        yield right

    
    def valid_box(self, box):
        return self.has_unique_nums(box)


    # List str -> Bool
    def has_unique_nums(self, array):
        seen_nums = set()
        for char in array:
            if char.isdigit():
                if char in seen_nums:
                    return False

                seen_nums.add(char)

        return True


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
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    t.run(s.isValidSudoku(board) == True)


    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    t.run(s.isValidSudoku(board) == False)

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]    
    t.run(s.isValidSudoku(board) == True)

    board = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
        ]
    t.run(s.isValidSudoku(board) == False)

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
    t.run(s.isValidSudoku(board) == True)