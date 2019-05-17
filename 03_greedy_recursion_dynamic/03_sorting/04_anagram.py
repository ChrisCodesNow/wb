'''
Approach 1:
    Build every substring of size |p|, checking for anagrams
    Edge Case: |p| > |s| => stop
Runtime: O(|s| |p|log|p|)
Space Complexity: O(|p|)
'''
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        front = 0
        back = len(p)
        indices = []
        while back <= len(s):
            if s == 'abab':
                print(front, back)
            window = s[front:back]
            if self.are_anagrams(window, p):
                indices.append(front)

            front += 1
            back += 1

        return indices


    def are_anagrams(self, s, p):
        return sorted(s) == sorted(p)



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


    string_s = "cbaebabacd" 
    string_p = "abc"
    t.run(s.findAnagrams(string_s, string_p) == [0, 6])

    string_s = "abab" 
    string_p = "ab"
    t.run(s.findAnagrams(string_s, string_p) == [0, 1, 2])





    