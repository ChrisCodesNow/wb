'''
Approach 1:
    Traverse grid:
        Connect land to adjacent land using disjoint set.
        Count distinct root elements that happen to be land.
Runtime: O(n^2)
Space Complexity: O(n^2)
'''
from union_find import UnionFind
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ds = self.connect_lands(grid)
        return self.count_disjoint_islands(grid, ds)
    

    def connect_lands(self, grid):
        m,n = len(grid), len(grid[0])
        ds = UnionFind(m * n)

        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                coord = (i,j)
                if self.is_land(grid, coord):
                    for v in self.get_neighbors(grid, coord):
                        if self.is_land(grid, v):
                            first = self.num(grid, coord)
                            second = self.num(grid, v)
                            ds.join(first, second)

        ds.compress()
        return ds


    def is_land(self, grid, coord):
        i,j = coord
        return grid[i][j] == '1'


    def get_neighbors(self, grid, coord):
        m,n = len(grid), len(grid[0])
        i,j = coord

        if i + 1 < m:
            yield (i + 1, j)
        if j + 1 < n:
            yield (i, j + 1)


    def num(self, grid, coord):
        n = len(grid[0])
        i,j = coord

        return i * n + j


    def count_disjoint_islands(self, grid, ds):
        roots = set(ds.get_parent())
        count = 0
        for num in roots:
            coord = self.to_coordinates(grid, num)
            if self.is_land(grid, coord):
                count += 1

        return count


    def to_coordinates(self, grid, num):
        n = len(grid[0])
        return num // n, num % n


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
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    count = 1
    t.run(s.numIslands(grid) == count)

    grid = []
    count = 0
    t.run(s.numIslands(grid) == count)