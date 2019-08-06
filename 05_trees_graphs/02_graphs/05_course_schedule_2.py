'''
Approach 1: BFS to get layer wise traversal and order
        Does this imply topological sort?

    algo(courses, edges):
        g = get adjacency list from edges
        in_g = get in degree count from edges and num courses
    
        src = all vertices with in degree of 0 at in_g

        Get BFS result @ (src, g)

    BFS(src, g):
        Q = Queue with all src elements
        visited = empty set

        Iterate Q:
            src - next in Q
            Mark src as visited
            Add src to ordered result
            Iterate neighbors v of src in g:
                v not yet visited:
                    Add v to Q

        Get ordered result
    
        
Runtime: O()
Space Complexity: O()
'''
from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.solution_01(numCourses, prerequisites)


    # ########################################
    # Approach 1
    #
    def solution_01(self, numCourses, prerequisites):
        g = self.adj_list(prerequisites)
        in_g = self.in_deg(prerequisites)

        src = [u for u in range(numCourses) if in_g[u] == 0]
        return self.BFS(src, g, numCourses)


    def adj_list(self, edges_rev):
        g = defaultdict(set)
        for v,u in edges_rev:
            g[u].add(v)
        return g


    def in_deg(self, edges_rev):
        in_g = defaultdict(int)
        for v,u in edges_rev:
            in_g[v] += 1
        return in_g

    
    def BFS(self, src, g, num_courses):
        order = []
        Q = deque(src[:])
        visited = set()

        while Q:
            u = Q.popleft()
            visited.add(u)
            order.append(u)

            if len(order) == num_courses:
                return order

            for v in g[u]:
                if v not in visited:
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
    solution = Solution()
    test = Test()


    num_courses = 2 
    prerequisites = [[1,0]] 
    result = [0,1]
    my_result = solution.findOrder(num_courses, prerequisites)
    test.run(my_result == result)


    num_courses = 4 
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    result = [[0,1,2,3], [0,2,1,3]]
    my_result = solution.findOrder(num_courses, prerequisites)
    test.run(my_result in result)