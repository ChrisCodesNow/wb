'''
Approach 1: BFS to get layer wise traversal and order
        Does this imply topological sort?

    algo(courses, edges):
        g = get adjacency list from edges
        in_g = get in degree count from edges and num courses
    
        src = all vertices with in degree of 0 at in_g

        Get BFS result @ (src, g)
        BFS result size = num courses size?

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

    # ########################################
    # Approach 1
    #

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