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


Approach 2: Bottom up Approach
Similar to approach 1, but use 2 arrays of size O(n) instead of grid of size O(m * n)

    m = size of string s
    n = size of string p
    top = False array of size n + 1
    bottom = False array of size n + 1

    Set end of s and p:
        Since s and p are both empy, bottom[-1] = True

    Set bottom array to (s empty, is P empty?):
        Iterate bottom array [n - 1 to 0]:
            Is next char a star and bottom[j + 2] = False
                bottom[j] = True
            Otherwise:
                bottom[j] = False

    Compute regex match:
    Iterate chars of s [m -1 to 0]:
        Iterate chars of p [n - 1 to 0]:
            p[j] has next wild char:
                s[i] equivalent to p[j]:
                    top[j] = zero or many tries, that is top[j + 2] or bottom[j]
                Otherwise:
                    top[j] = zero tries, that is top[j + 2]
            Otherwise:
                s[i] equivalent to p[j]:
                    top[j] = next match, that is bottom[j + 1]
                Otherwise:
                    top[j] = False
        bottom array = copy of top array
    

Runtime: O(mn)
Space Complexity: O(m)
'''
from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # return self.solution_01(s, p)
        return self.solution_02(s, p)


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
    
    # ########################################
    # Approach 2
    #
    def solution_02(self, s, p):
        m = len(s)
        n = len(p)

        top = self.false_array(n + 1)
        bottom = self.false_array(n + 1)

        self.set_end_s_p_02(bottom)
        self.set_bottom_row(bottom, p, n)
        return self.compute_match_02(top, bottom, s, p, m, n)


    def false_array(self, num_elements):
        return [False for _ in range(num_elements)]


    def set_end_s_p_02(self, bottom):
        bottom[-1] = True


    def set_bottom_row(self, bottom, p, n):
        for j in range(n - 1, -1, -1):
            bottom[j] = self.has_next_star(p, j) and bottom[j + 2] == True
    
    def compute_match_02(self, top, bottom, s, p, m ,n):
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if self.has_next_star(p, j):
                    if self.are_equivalent(s[i], p[j]):
                        top[j] = top[j + 2] or bottom[j]
                    else:
                        top[j] = top[j + 2]
                else:
                    if self.are_equivalent(s[i], p[j]):
                        top[j] = bottom[j + 1]
                    else:
                        top[j] = False
            bottom = top[:]
        
        return top[0]



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