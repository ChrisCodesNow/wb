'''
Approach 1: 2 Finger algorithm
    Swap front and back chars

Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front = 0
        back = len(s) - 1

        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1


# Test
if __name__ == '__main__':
    s = Solution()

    # Check for in place reversing through id()
    l = ["h","e","l","l","o"]
    old_id = id(l)
    s.reverseString(l)
    print(l == ["o","l","l","e","h"] and old_id == id(l))

    l = ["H","a","n","n","a","h"]
    old_id = id(l)
    s.reverseString(l)
    print(l == ["h","a","n","n","a","H"] and old_id == id(l))