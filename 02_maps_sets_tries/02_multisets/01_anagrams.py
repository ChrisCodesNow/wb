'''
Approach 1:
    Get counter on P, update counter on shifting window checking for anagram
Runtime: O(sp)
Space Complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(p) > len(s):
            return []

        indices = []
        p_count = Counter(p)
        window = Counter(s[:len(p)])

        left = 0
        right = len(p) - 1
        while right < len(s) - 1:
            if p_count == window:
                indices.append(left)

            old_left = s[left]
            left += 1
            right += 1
            self.update_window(window, old_left, s[right])

        if p_count == window:
            indices.append(left)

        return indices


    def update_window(self, window, doomed, added):
        window[doomed] -= 1
        if not window[doomed]:
            del window[doomed]

        window.update(added)

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


    string = "cbaebabacd"
    p = "abc"
    t.run(s.findAnagrams(string, p) == [0, 6])

    string = "abab" 
    p = "ab"
    t.run(s.findAnagrams(string, p) == [0, 1, 2])

    string = ""
    p = "abc"
    t.run(s.findAnagrams(string, p) == [])

    string = 'abcdabcd'
    p = 'abcdabcda'
    t.run(s.findAnagrams(string, p) == [])

    string = 'abcdeacbkda'
    p = 'a'
    t.run(s.findAnagrams(string, p) == [0, 5, 10])