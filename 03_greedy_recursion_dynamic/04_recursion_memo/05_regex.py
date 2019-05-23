'''
Approach 1:
    At each char i in s and char j in p either:
    1. char i + 1 is wild char *
        Match 0 or more chars j in s
    2. char i = char j or char j is single wild char .
        Recursively check next chars i and j
    3. char i != char j
        Recursively check char i and char j + 1

    Base Cases:
    1. At end of s and p
        Stop
    2. At end of s
        Check remaining of p j to n - 1 is empty pattern
    3. AT end of p
        Check remaining of s i to m - 1 is mepty pattern

Runtime: O()
Space Complexity: O()
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solution_01(s, p)


    # ########################################
    # Approach 1
    #
    def solution_01(self, s, p):
        # if not s and not p:
        #     return True
        # elif not s:
        #     return p == '.*'
        # elif not p:
        #     return s == '.*'

        return self.regex_01(s, p, 0, 0)

    
    def regex_01(self, s, p, i, j):
        if i == len(s) and j == len(p):
            return True
        elif i == len(s):
            return self.is_empty_pattern(p, j)
        elif j == len(p):
            return self.is_empty_pattern(s, i)

        if self.has_next_wild(p, j):
            i_end = self.get_pattern_end(s, p, i, j)
            for ki in range(i, i_end + 1):
                if self.regex_01(s, p, ki, j + 2):
                    return True
            return False
        elif s[i] == p[j] or p[j] == '.':
            return self.regex_01(s, p, i + 1, j + 1)
        else:
            return self.regex_01(s, p, i, j + 1)


    def get_pattern_end(self, s, p, i, j):
        prev_p = p[j]
        if prev_p == '.':
            return len(s)
        
        for i_end in range(i, len(s)):
            if s[i_end] != prev_p:
                return i_end
        return len(s)


    # Determine if substring from idx to n-1 is empty
    def is_empty_pattern(self, string, idx):
        if idx == len(string):
            return True

        substr = string[idx:]
        if len(substr) == 2 and substr[-1] == '*':
            return True
        else:
            return False


    # Determine if char j is before wild char *
    def has_next_wild(self, p, j):
        if j < len(p) - 1:
            return p[j + 1] == '*'
        
        return False


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
    t.run(s.isMatch(string_s, p) == True)

    string_s = "aab"
    p = "c*a*b"
    t.run(s.isMatch(string_s, p) == True)

    string_s = "mississippi"
    p = "mis*is*p*."
    t.run(s.isMatch(string_s, p) == False)

    string_s = "aaa"
    p = "ab*a"
    t.run(s.isMatch(string_s, p) == False)
    
    string_s = "aaa"
    p = "a*a"
    t.run(s.isMatch(string_s, p) == True)

    string_s = "a"
    p = "ab*"
    t.run(s.isMatch(string_s, p) == True)


    string_s = "bbbba"
    p = ".*a*a"
    t.run(s.isMatch(string_s, p) == True)

    string_s = "b"
    p = "aaa."
    t.run(s.isMatch(string_s, p) == False)