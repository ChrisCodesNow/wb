'''
Approach 1:
    Get in adjaceny list and in degree from edges
    Do modified BFS: Khan's topological sort
        Initialize Q with vertices v of in degree 0
        Loop Q:
            Remove outgoing edges of current vertex u
            Add v to Q if it has in degree of 0
Runtime: O(V + E)
Space Complexity: O(V + E)
'''
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = self.adj_list(prerequisites)
        in_deg = self.in_degree(prerequisites)
        order = self.top_sort(g, in_deg, numCourses)
        return len(order) == numCourses


    def adj_list(self, in_edges):
        g = defaultdict(set)
        for v,u in in_edges:
            g[u].add(v)

        return g


    def in_degree(self, in_edges):
        in_deg = defaultdict(set)
        for v,u in in_edges:
            in_deg[v].add(u)

        return in_deg

    
    # Khan's algorithm for topological sort
    def top_sort(self, g, in_deg, n):
        zeros = [u for u in range(n) if not in_deg[u]]

        order = []
        Q = deque(zeros)
        while Q:
            u = Q.popleft()
            order.append(u)
            for v in in_deg:
                if u in in_deg[v]:
                    in_deg[v].remove(u)
                    if not in_deg[v]:
                        Q.append(v)

        return order


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

    n = 2
    prerequisites = [[1,0]] 
    t.run(s.canFinish(n, prerequisites) == True)

    n = 2
    prerequisites = [[1,0], [0, 1]] 
    t.run(s.canFinish(n, prerequisites) == False)

    n = 1
    prerequisites = [] 
    t.run(s.canFinish(n, prerequisites) == True)

    n = 3
    prerequisites = [[1,0]] 
    t.run(s.canFinish(n, prerequisites) == True)

    n = 3
    prerequisites = [[0,1],[0,2],[1,2]]
    t.run(s.canFinish(n, prerequisites) == True)

    n = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    t.run(s.canFinish(n, prerequisites) == False)

    n = 4
    prerequisites = [[0,1],[3,1],[1,3],[3,2]]
    t.run(s.canFinish(n, prerequisites) == False)

    n = 8
    prerequisites = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]
    t.run(s.canFinish(n, prerequisites) == False)