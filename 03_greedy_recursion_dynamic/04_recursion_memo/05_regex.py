from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solution_01(s, p)


    # ########################################
    # Approach 1
    #
    def solution_01(self, s, p):
        if not s and not p:
            return True
        elif not s:
            return p == '.*'
        elif not p:
            return s == '.*'

        return self.regex_01(s, p, 0, 0)

    
    def regex_01(self, s, p, i, j):
        if i == len(s) and j == len(p):
            return True
        elif i == len(s) or j == len(p):
            return False

        if s[i] == p[j]:
            return self.regex_01(s, p, i + 1, j + 1)
        elif p[j] == '*':
            prev_char = p[j - 1]
            i_end = self.get_pattern_end(s, p, i, j, prev_char)
            return self.regex_01(s, p, i, j + 1) or \
                    self.regex_01(s, p, i_end, j + 1)
        elif p[j] == '.':
            return self.regex_01(s, p, i + 1, j + 1)
        else:
            return self.regex_01(s, p, i, j + 1)


    def get_pattern_end(self, s, p, i, j, prev_char):
        if prev_char == '.':
            return len(s)
        
        for i_end in range(i, len(s)):
            if s[i_end] != prev_char:
                return i_end
        else:
            return len(s)


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


    string_s = "aa"
    p = "a"
    t.run(s.isMatch(string_s, p) == False)

    string_s = "aa"
    p = "a*"
    t.run(s.isMatch(string_s, p) == True)

    string_s = "ab"
    p = ".*"
    #Failed
    t.run(s.isMatch(string_s, p) == True)

    string_s = "aab"
    p = "c*a*b"
    #Failed
    t.run(s.isMatch(string_s, p) == True)

    string_s = "mississippi"
    p = "mis*is*p*."
    t.run(s.isMatch(string_s, p) == False)