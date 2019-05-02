'''
Approach 1:
    Iterate from back
    Accumulate total: val of char * 26 ** position
Runtime: O(c), all c chars in title
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def titleToNumber(self, s: str) -> int:
        return self.solution_01(s)
        return self.solution_02(s)

    def solution_01(self, title):
        total = 0
        for i, char in enumerate(list(reversed(title))):
            total +=  self.col_val(char) * 26 ** i

        return total
        
    def col_val(self, char):
        return (ord(char) - 65) + 1

# Test
if __name__ == '__main__':
    s = Solution()

    title = "A"
    print(s.titleToNumber(title) == 1)
    
    title = "AB"
    print(s.titleToNumber(title) == 28)

    title = "ZY"
    print(s.titleToNumber(title) == 701)
    
    title = "A"
    print(s.titleToNumber(title) == 1)