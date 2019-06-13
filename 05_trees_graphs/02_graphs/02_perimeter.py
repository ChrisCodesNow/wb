'''
Approach 1:
    Modified BFS:
        Count perimeter of each land square
Runtime: O(V + E)
Space Complexity: O(V)
'''
from typing import List
from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        src = self.find_land(grid)
        if src:
            visited = set([src])
        Q = deque([src])
        perimeter = 0
        while Q:
            u = Q.popleft()
            perimeter += self.count_perimeter(grid, u)
            for v in self.neighbors(grid, u):
                if v not in visited and self.is_land(grid, v):
                    Q.append(v)
                    visited.add(v)
        
        return perimeter


    def find_land(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.is_land(grid, (i,j)):
                    return (i, j)


    def count_perimeter(self, grid, u):
        p = 0
        for v in self.adjacent(u):
            if not self.in_graph(grid, v) or self.is_water(grid, v):
                p += 1

        return p


    # Gets neighbors up, down, left, right
    def neighbors(self, grid, u):
        m,n = len(grid), len(grid[0])
        i,j = u

        if i - 1 >= 0:
            yield (i - 1, j)
        if i + 1 < m:
            yield (i + 1, j)
        if j - 1 >= 0:
            yield (i, j - 1)
        if j + 1 < n:
            yield (i, j + 1)


    def is_land(self, grid, u):
        i,j = u
        return grid[i][j] == 1

    
    def adjacent(self, u):
        i,j = u

        yield (i - 1, j)
        yield (i + 1, j)
        yield (i, j - 1)
        yield (i, j + 1)


    def in_graph(self, grid, u):
        m,n = len(grid), len(grid[0])
        i,j = u

        return (0 <= i and i < m) and (0 <= j and j < n)


    def is_water(self, grid, u):
        i,j = u
        return grid[i][j] == 0

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

    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    t.run(s.islandPerimeter(grid) == 16)
