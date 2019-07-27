'''
Approach 1:
n = size of board
nQueens(board, placed, row):
    Base case:
        Row out of range and placed Queens = n:
        => 1
    
    solutions = 0
    Iterate cols j [0 to n - 1]:
        Queen at (row, j) not threaten placed Queens:
            Place Queen in board and mark as placed
            solutions += Recursive compute nQueens at next row
            Remove placed Queen (row, j)

    Get solutions


Runtime: O()
Space Complexity: O()
'''
# ########################################
# Approach 1
#
def nqueens(n):
    placed = set()
    return nqueens_solutions(n, placed, 0)


def nqueens_solutions(n, placed, row):
    if row >= n and len(placed) == n:
        # Row out of bounds only when all n Queens are placed
        return 1
    
    solutions = 0
    for j in range(n):
        q = (row, j)
        if not threatens(q, n, placed):
            placed.add(q)
            solutions += nqueens_solutions(n, placed, row + 1)
            placed.remove(q)
    
    return solutions


def threatens(q, n, placed):
    path = rows(q, n) + cols(q, n) + \
            negative_diagonal(q, n) + \
            positive_diagonal(q, n)

    return any (coord in placed for coord in path)


def rows(q, n):
    i,j = q
    return [(i, col) for col in range(n)]


def cols(q, n):
    i,j = q
    return [(row, j) for row in range(n)]


def negative_diagonal(q, n):
    return up_left(q) + down_right(q, n)


def up_left(q):
    i,j = q
    i,j = i - 1, j - 1

    coords = []
    while i >= 0 and j >= 0:
        coords.append((i,j))
        i,j = i - 1, j - 1
    
    return coords


def down_right(q, n):
    i,j = q
    i,j = i + 1, j + 1

    coords = []
    while i < n and j < n:
        coords.append((i,j))
        i,j = i + 1, j + 1

    return coords


def positive_diagonal(q, n):
    return down_left(q, n) + up_right(q, n)


def down_left(q, n):
    i,j = q
    i,j = i + 1, j - 1

    coords = []
    while i < n and j >= 0:
        coords.append((i,j))
        i,j = i + 1, j - 1

    return coords


def up_right(q, n):
    i,j = q
    i,j = i - 1, j + 1

    coords = []
    while i >= 0 and j < n:
        coords.append((i,j))
        i,j = i - 1, j + 1

    return coords



# Test
class Test:
    count = 0
    def run(self, result):
        self.count += 1
        if result:
            print(f"Passed test {self.count}")
        else:
            print(f"Failed test {self.count}")

        
from time import time
if __name__ == '__main__':
    start = time()
    test = Test()


    n = 1
    result = 1
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 2
    result = 0
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 3
    result = 0
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 4
    result = 2
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 5
    result = 10
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 6
    result = 4
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 7
    result = 40
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 8
    result = 92
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 9
    result = 352
    my_result = nqueens(n)
    test.run(result == my_result)

    n = 10
    result = 724
    my_result = nqueens(n)
    test.run(result == my_result)
    end = time()

    print(f"Test took {end - start} seconds")