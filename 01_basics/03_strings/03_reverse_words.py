'''
Approach 1:
    Separate words, reverse their individual order

Approach 2:
    Same as approach 1, but use map instead of iteration

Runtime: O(nw)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        return self.solution_01(s)
        # return self.solution_02(s)

    def solution_01(self, s):
        words = s.split()
        for i in range(len(words)):
            words[i] = self.reverse_string(words[i])

        return ' '.join(words)

    def solution_02(self, s):
        words = s.split()
        words = list(map(self.reverse_string, words))
        return ' '.join(words)

    # Runtime: O(w), for string with w chars
    def reverse_string(self, string):
        return string[::-1]


# Test
if __name__ == '__main__':
    s = Solution()

    string = "Let's take LeetCode contest"
    print(s.reverseWords(string) == "s'teL ekat edoCteeL tsetnoc")

    string = "this is first sent"
    print(s.reverseWords(string) == "siht si tsrif tnes")
    