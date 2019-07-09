'''
Approach 1: recursion with memo, backtracking
    Base 1: Both str empty => T
    Base 2: Only S or only p empty => F
    Base 3: s,p in memo => Get memoized response


    P has next wild character:
        Recursively match zero times, that is s, p[2:]
        or
        Recursively match many times (one at a time), that is s[1:], p
        Any of them lead to match?
        Memoize response
    P does not have next wild character:
        Direct match: by char or by dot:
            Recursively match s[1:], p[1:]
            Memoize reponse

        Not match:
            Recursively match s, p[1:]
            Memoize reponse

Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        return self.match(s, p, memo)

    def match(self, s, p, memo):
        # Base cases
        if not s and not p:
            return True
        elif not s:
            return self.is_empty(p)
        elif not p:
            return self.is_empty(s)
        elif (s, p) in memo:
            return memo[s, p]

        # Recursive cases
        # Next is wild
        if self.has_next_wild(p):
            # Match 0 or more times (1 at a time)
            zero = self.match(s, p[2:], memo)
            if self.are_equivalent(s[0], p[0]):
                many = self.match(s[1:], p, memo)
            else:
                many = False
            memo[s, p] = zero or many
        else:
            # Match char by char
            if self.are_equivalent(s[0], p[0]):
                memo[s, p] = self.match(s[1:], p[1:], memo)
            else:
                memo[s,p] = False
                # memo[s,p] = self.match(s, p[1:], memo)

        return memo[s, p]


    def is_empty(self, s):
        if not s:
            return True
        elif len(s) >= 2 and s[1] == "*":
            return self.is_empty(s[2:])
        else:
            return False

        
    def has_next_wild(self, p):
        return len(p) >= 2 and p[1] == "*"


    def are_equivalent(self, char_s, char_p):
        return char_p == '.' or char_s == char_p


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