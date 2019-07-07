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


Approach 2:
    Similar as approach 1, but use count sort instead of comparison based sorting

    Use a window of size P
    Traverse S using window:
        Add next right value from S
        Sorted window is same as sorted P:
            Save current left index
        Remove left value of window

    Get all saved incides
Runtime: O(SP)
Space Complexity: O(S + P)
'''
from typing import List
from collections import deque
from count_sort import get_histogram
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return self.solution_01(s, p)
        return self.solution_02(s, p)

    # ########################################
    # Approach 1
    #
    def solution_01(self, s, p):
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

        
    # ########################################
    # Approach 2
    #
    def solution_02(self, s, p):
        if not s or len(s) < len(p):
            return []

        alphabet_size = 26

        window = self.to_indices(s[:len(p) - 1])
        sorted_window = get_histogram(window, alphabet_size)
        sorted_p = get_histogram(self.to_indices(p), alphabet_size)

        right = len(p) - 2
        num_windows = len(s) - len(p) + 1
        anagram_indices = []
        for left in range(num_windows):
            right += 1
            self.increment(sorted_window, s[right])
            if sorted_window == sorted_p:
                anagram_indices.append(left)

            self.decrement(sorted_window, s[left])

        return anagram_indices



    def to_indices(self, alphabet_chars):
        return list(map(self.idx, alphabet_chars))


    def increment(self, histogram, char):
        i = self.idx(char)
        histogram[i] += 1

    
    def decrement(self, histogram, char):
        i = self.idx(char)
        histogram[i] -= 1


    def idx(self, char):
        return ord(char) - ord('a')


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