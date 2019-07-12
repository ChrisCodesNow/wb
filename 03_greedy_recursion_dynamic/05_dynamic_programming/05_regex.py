'''
Approach 1: Bottom up Approach
    m = size of string s
    n = size of string p
    grid = False array of size (m + 1) x (n + 1)

    Set end of S and P, that is grid[m, n] = True

    Set last row(end of s, is P empty?):
        Iterate last row, on cols j [n - 1 to 0]:
            p[last row, j] = Is curr p empty, that is (p[j + 1] = * and grid[j + 2] = True)

    # Set last col to all false (Done by default when creating False array)

    Compute regex match:
        Iterate rows [m - 1 to 0]:
            Current p has next star (p[j + 1] = *)?:
                Current s and p char are equivalent OR p char is dot:
                    grid[i, j] = zero or more times, 
                    that is grid[i, j + 2] or grid[i + 1, j]
                Otherwise:
                    grid[i, j] = zero times,
                    that is grid[i, j + 2]
            Otherwise:
                Current s and p char are equivalent OR p char is dot:
                    grid[i,j] = next match, 
                    that is grid[i + 1, j + 1]
                Otherwise:
                    grid[i, j] = False, that is no match!

    Regex match = grid[0, 0]

Runtime: O(mn)
Space Complexity: O(mn)
'''
from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solution_01(s, p)


    # ########################################
    # Approach 1
    #
    def solution_01(self, s, p):
        m = len(s)
        n = len(p)
        grid = self.make_false_grid(m + 1, n + 1)

        self.set_end_s_p(grid)
        self.set_last_row(grid, p, n)
        
        return self.compute_match(grid, s, p, m, n)


    def make_false_grid(self, rows, cols):
        return [ [False for _ in range(cols)] \
                for __ in range(rows)]


    def set_end_s_p(self, grid):
        grid[-1][-1] = True


    # Check if p[j] is empty or not dynamically
    def set_last_row(self, grid, p, n):
        for j in range(n - 1, -1, -1):
            grid[-1][j] = self.has_next_star(p, j) and \
                        grid[-1][j + 2] == True


    def compute_match(self, grid, s, p, m, n):
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if self.has_next_star(p, j):
                    if self.are_equivalent(s[i], p[j]):
                        grid[i][j] = grid[i][j + 2] or grid[i + 1][j]
                    else:
                        grid[i][j] = grid[i][j + 2]
                else:
                    if self.are_equivalent(s[i], p[j]):
                        grid[i][j] = grid[i + 1][j + 1]
                    else:
                        grid[i][j] = False

        return grid[0][0]


    def has_next_star(self, p, j):
        if j < len(p) - 1:
            return p[j + 1] == '*'
        else:
            return False


    def are_equivalent(self, s_char, p_char):
        return s_char == p_char or p_char == '.'
    

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


    s = "aa"
    p = "a"
    result = False
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "aa"
    p = "a*"
    result = True   
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "ab"
    p = ".*"
    result = True
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "aab"
    p = "c*a*b"
    result = True
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "mississippi"
    p = "mis*is*p*."
    result = False
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "a"
    p = "ab*"
    result = True
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "bbbba"
    p = ".*a*a"
    result = True
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "ab"
    p = ".*c"
    result = False
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "b"
    p = "aaa."
    result = False
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = ""
    p = "c*c*"
    result = True
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)

    s = "a"
    p = ".*..a*"
    result = False
    my_result = solution.isMatch(s, p)
    test.run(result == my_result)