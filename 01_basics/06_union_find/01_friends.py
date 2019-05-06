
'''
Approach 1:
    Get edges (without repetition), find all subsets, and count number of 
    distinct subsets

Runtime: O(V^2)
Space Complexity: O()
'''
from typing import List
from union_find import UnionFind

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        edges = self.get_edges(M)
        subsets = self.build_disjoint_set(len(M), edges)
        return self.count_distinct_subsets(subsets)


    # Runtime: O(V^2)
    def get_edges(self, M):
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j]:
                    yield (i, j)


    # Runtime: O(E)
    def build_disjoint_set(self, num_vertices, edges):
        ds = UnionFind(num_vertices)
        for u, v in edges:
            root_u = ds.find(u)
            root_v = ds.find(v)
            if root_u != root_v:
                ds.join(root_u, root_v)

        return ds

    # O(V)
    def count_distinct_subsets(self, ds):
        ds.compress()
        distinct_subsets = set(ds.get_parent())
        return len(distinct_subsets)

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

    M = [[1,1,0],
        [1,1,0],
        [0,0,1]]
    t.run(s.findCircleNum(M) == 2)

    M = [[1,1,0],
        [1,1,1],
        [0,1,1]]
    t.run(s.findCircleNum(M) == 1)

    M = [[1,1,1],
        [1,1,1],
        [1,1,1]]
    t.run(s.findCircleNum(M) == 1)

    M = [[1,0,1],
        [0,1,1],
        [1,1,1]]
    t.run(s.findCircleNum(M) == 1)


    M = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]
    t.run(s.findCircleNum(M) == 3)

    M = []
    t.run(s.findCircleNum(M) == 0)