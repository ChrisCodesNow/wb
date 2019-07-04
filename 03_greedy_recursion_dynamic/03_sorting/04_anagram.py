'''
Approach 1:
    S empty => No anagrams

    front = 0
    back = len(p) - 2
    Sort p.
    window = Dummy_front + S from [front up to back].

    Traverse S as windows:
        Move front and back to next values.
        Remove window's left value.
        Add current back character to window.
        Sorted window = sorted p:
            Save start index.
    
    Get all saved indices.

Runtime: O(S * PlogP)
Space Complexity: O(S)
'''
from typing import List
from collections import deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p):
            return []

        indices = []
        sorted_p = sorted(p)
        initial_s = list(s[:len(p) - 1])
        window = deque(["dummy"] + initial_s)

        back = len(p) - 2
        last_front = len(s) - len(p)
        for front in range(last_front + 1):
            back += 1
            window.popleft()
            window.append(s[back])
            if sorted(window) == sorted_p:
                indices.append(front)

        return indices
        
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


    s = "cbaebabacd" 
    p = "abc"
    result = [0, 6]
    my_result = solution.findAnagrams(s, p)
    test.run(result == my_result)


    s = "abab" 
    p = "ab"
    result = [0, 1, 2]
    my_result = solution.findAnagrams(s, p)
    test.run(result == my_result)
