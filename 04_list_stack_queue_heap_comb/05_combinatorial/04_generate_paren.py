'''
Approach 1:
    Get all balanced parentheses of size n - 1.
    Wrap current balanced parentheses around all prev balanced parentheses substrings.
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        else:
            prev_balanced = self.generateParenthesis(n - 1)
            curr_balanced = []
            for prev_bal in prev_balanced:
                # Current balanced parentheses are larger by 1 than prev balanced
                for i in range(len(prev_bal) + 1):
                    if self.is_balanced(prev_bal[:i]):
                        curr_paren = '(' + prev_bal[:i] + ')' + prev_bal[i:]
                        curr_balanced.append(curr_paren)
            
            return curr_balanced


    # paren gauranteed to be a bal paren or a substring of one.
    # Thus, easier to validate
    def is_balanced(self, paren):
        unbal_count = 0
        for p in paren:
            if p == '(':
                unbal_count += 1
            else:
                unbal_count -= 1
        
        return unbal_count == 0


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

    n = 3
    answer = [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]
    output = s.generateParenthesis(n)
    t.run(sorted(output) == sorted(answer))