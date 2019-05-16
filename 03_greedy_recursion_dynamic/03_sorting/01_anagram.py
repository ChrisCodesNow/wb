'''
Approach 1:
    Compare sorted strings
Runtime: O(nlogn)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


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


    string_s = "anagram"
    string_t = "nagaram"
    t.run(s.isAnagram(string_s, string_t) == True)

    string_s = "rat"
    string_t = "car"
    t.run(s.isAnagram(string_s, string_t) == False)
