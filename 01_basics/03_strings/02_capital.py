'''
Approach 1:
    Determine if input string is either
    uppercase, lowercase, or camel case.

Runtime: O(n)
Space Complexity: O(n), for temporary string creation
'''
from typing import List
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or \
            word == word.lower() or \
            word == word.capitalize():
            return True

        return False

# Test
if __name__ == '__main__':
    s = Solution()

    # Upper => T
    word = "USA"
    print(s.detectCapitalUse(word))

    # Neither => False
    word = "FlaG"
    print(s.detectCapitalUse(word))

    # CApitalized => True
    word = "Flag"
    print(s.detectCapitalUse(word))

    # Lower => True
    word = "welcome"
    print(s.detectCapitalUse(word))