'''
Approach 1:
    Modified BFS
    Get start location of 1st letter in grid.
    DFS on each start location:
        current char on board == char search:
            Continue BFS on next char of word
            Any of paths build entire word?

    Else: False

Approach 2: DFS with backtracking
    seach(board, word):
        coords = find all coordinates in board with char = word[0]
        Iterate src coords:
            visited = empty set
            built_word = word[0]
            target = word
            DFS(board, src coord, visited, built_word, target)
            Did DFS find word?:
                => True
        None of src coords found word:
            => False

    dfs(board, source, visited, built_word, target):
        built_word = target?:
            => True
        Mark source as visited
        Iterate neighbors v of source:
            v not visited:
                next_word = built_word + char @ board[v]
                Rec dfs(source = v, built_word = next_word)
                Did dfs find word?:
                    => True

        Remove source from visited
        Word not found in this path:
            => False

Runtime: O()
Space Complexity: O()
'''
from collections import deque
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # return self.solution_01(board, word)
        return self.solution_02(board, word)
        
        
    # ########################################
    # Approach 1
    #
    def solution_01(self, board, word):
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
            if word == "ABCESEEEFS":
                print(f"u = {u}, idx = {idx}")
            if board[i][j] == word[idx]:
                visited.add(u)          # Mark as visited once word in current location is used
                if idx == len(word) - 1:
                    return True
                else:
                    for v in self.get_neighbors(board, u):
                        if v not in visited:
                            Q.append((v, idx + 1))
        return False


    # ########################################
    # Approach 2
    #
    def solution_02(self, board, word):
        coords = self.get_locations(board, word[0])

        for coord in coords:
            visited = set()
            if self.dfs(board, coord, visited, word[0], word):
                return True

        return False

    
    def dfs(self, board, coord, visited, built_word, target):
        if built_word == target:
            return True
        visited.add(coord)
        for v in self.get_neighbors(board, coord):
            if v not in visited:
                i,j = v
                next_word = built_word + board[i][j]
                if self.dfs(board, v, visited, next_word, target):
                    return True

        visited.remove(coord)
        return False


    # ########################################
    # Mutual methods
    #
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


    # BUG: This needs to be a backtracking algorithm!
    # Study how this is done, then come back!
    board = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]
    word = "ABCESEEEFS"
    t.run(s.exist(board, word) == True)