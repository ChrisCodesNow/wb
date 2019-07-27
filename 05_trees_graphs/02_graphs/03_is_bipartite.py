'''
Approach 1:
    Modified BFS:
        Join all neighbors v of u among themselves
        Validate u and all its neighbors v are not connected (disjoint)
        Add unvisited nieghbors to Q ... BFS

    All valid => T
    

Approach 2:
    V0 = set representing first group coloring vertex
    V2 = set representing second group coloring vertex

    g = adjacency list from input graph format
    src = 0
    color = 0
    visited = set
    compute modified bfs(g, src, visited, V0, V1, color)

    bfs(g, src, visited, V0, V1, color):
        color = 0?:
            Add src to set V0
        color = 1?:
            Add src to set V1

        Mark src as visited
        next_color = (color + 1) mod 2
        Iterate neighbors v of g[src]:
            v has not been visited:
                compute dfs with (src = v, color = next color)
                Can't color appropriately?:
                    => Not bipartite => False

            Validate src and v are in distinct sets V0 and V1

        Can color all =? True
    
Runtime: O(V + E)
Space Complexity: O(V + E)
'''
from collections import defaultdict, deque
from typing import List
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]


    def find(self, a):
        '''
        Get root node/parent node of a
        '''
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


    def join(self, b, a):
        '''
        Make root of a parent of root of b
        '''
        parent_a = self.find(a)
        parent_b = self.find(b)
        self.parent[parent_b] = parent_a


    def are_connected(self, a, b):
        return self.find(a) == self.find(b)

    def distinct_sets(self):
        return len(set(self.parent))


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # return self.solution_01(graph)
        return self.solution_02(graph)

    # ########################################
    # Approach 1
    #
    def solution_01(self, graph):
        g = self.adj_list(graph)
        src = self.get_src(g)
        visited = set([src])
        Q = deque([src])
        ds = DisjointSet(len(graph))
        while Q:
            u = Q.popleft()
            self.join_neighbors(g, u, ds)
            if not self.validate_bipartite(g, u, ds):
                return False

            for v in g[u]:
                if v not in visited:
                    Q.append(v)
                    visited.add(v)

        return True


    def get_src(self, g):
        for u in g:
            if g[u]:
                return u
        
        return 0


    def join_neighbors(self, g, u, ds):
        neighbors = list(g[u])
        if neighbors:
            root = neighbors[0]
            for v in neighbors:
                ds.join(v, root)


    def validate_bipartite(self, g, u, ds):
        for v in g[u]:
            if ds.are_connected(u, v):
                return False
        
        return True

    # ########################################
    # Approach 2
    #
    def solution_02(self, graph):
        V0 = set()
        V1 = set()
        g = self.adj_list(graph)
        src = 0
        color = 0
        visited = set()

        return self.dfs(g, src, visited, V0, V1, color)


    def dfs(self, g, src, visited, V0, V1, color):
        if color == 0:
            V0.add(src)
        else:
            V1.add(src)

        visited.add(src)
        next_color = (color + 1) % 2
        for v in g[src]:
            if v not in visited:
                if not self.dfs(g, v, visited, V0, V1, next_color):
                    return False
            if (src in V0 and v in V0) or (src in V1 and v in V1):
                return False

        return True


    # ########################################
    # Mutual methods
    #
    def adj_list(self, edges):
        g = defaultdict(set)
        for u,outgoing in enumerate(edges):
            for v in outgoing:
                g[u].add(v)
                g[v].add(u)

        return g


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

    edges = [[1,3], [0,2], [1,3], [0,2]]
    t.run(s.isBipartite(edges) == True)

    edges = [[1,2,3], [0,2], [0,1,3], [0,2]]
    t.run(s.isBipartite(edges) == False)

    edges = [[1],[0,3],[3],[1,2]]
    t.run(s.isBipartite(edges) == True)

    edges = [[],[3],[],[1],[]]
    t.run(s.isBipartite(edges) == True)

    edges = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    t.run(s.isBipartite(edges) == False)

    edges = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
    t.run(s.isBipartite(edges) == False)