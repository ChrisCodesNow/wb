'''
Approach 1:
    Modified bfs, count distinct lands

Runtime: O(mn)
Space Complexity: O(mn)

Note: Verify runtinme and space complexity
'''
from typing import List
from union_find import UnionFind
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ds = self.modified_bfs(grid)
        return self.count_distinct_islands(grid, ds)

    
    # Build disjoint set of connected components
    def modified_bfs(self, grid):
        visited = set()
        Q = deque(self.get_land_coordinates(grid))
        
        # BFS modification
        m, n = self.grid_dimmensions(grid)
        ds = UnionFind(n * m)

        # first grid element
        visited.add((0, 0))
        Q.append((0, 0))

        while Q:
            u = Q.popleft()
            for v in self.get_neighbors(u, grid):
                if v not in visited:
                    if self.are_adjacent_land(u, v, grid):
                        self.connect_land(u, v, ds, grid)

                    visited.add(v)

        return ds

    
    # Count islands, ignoring bodies of water
    def count_distinct_islands(self, grid, ds):
        ds.compress()
        distinct_subsets = set(ds.get_parent())

        m, n = self.grid_dimmensions(grid)
        count = 0
        for ele_id in distinct_subsets:
            i = self.id_row(ele_id, n)
            j = self.id_col(ele_id, n)
            if grid[i][j]:
                count += 1

        print(ds.get_parent())
        return count


    def grid_dimmensions(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        return rows, cols


    # Get valid neighbors of input grid element
    def get_neighbors(self, u, grid):
        i, j = u
        m, n = self.grid_dimmensions(grid)

        # Up, down, left, right
        if 0 <= i - 1:
            yield (i - 1, j)
        if i + 1 < m:
            yield (i + 1, j)
        if 0 <= j - 1:
            yield (i, j - 1)
        if j + 1 < n:
            yield (i, j + 1)


    # Get all land coordinates on grid
    def get_land_coordinates(self, grid):
        land_coordinates = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    land_coordinates.append((i, j))

        return land_coordinates


    # Check if adjacent elements are land
    def are_adjacent_land(self, u, v, grid):
        i_u, j_u = u
        i_v, j_v = v

        if grid[i_u][j_u] and grid[i_v][j_v]:
            return True
        
        return False


    # Join adjacent subsets of land
    def connect_land(self, u, v, ds, grid):
        i_u, j_u = u
        i_v, j_v = v
        m, n = self.grid_dimmensions(grid)

        id_u = self.row_col_id(u, n)
        id_v = self.row_col_id(v, n)

        ds.join(id_u, id_v)


    # Get enumerated grid element's row value
    def id_row(self, ele_id, cols):
        return ele_id // cols


    # Get enumerated grid element's col value
    def id_col(self, ele_id, cols):
        return ele_id % cols


    # Get enumerated grid element from its row and columns
    def row_col_id(self, u, cols):
        i, j = u
        ele_id = cols * i + j

        return ele_id



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


# BUG: id(8) is not being tied to main island..
# [3, 3, 3, 3, 4, 3, 3, 7, 8, 9, 3,   3, 12, 13, 14, 15, 16, 17, 18, 19]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    grid = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]
    t.run(s.numIslands(grid) == 1)
    

    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]

    t.run(s.numIslands(grid) == 3)


    grid = []
    t.run(s.numIslands(grid) == 0)