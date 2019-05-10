'''
Approach 1:
    Count char frequency, get first unique
    Edge Case: Emtpy string
Runtime: O(n)
Space Complexity: O(n)
'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        char_frequency = Counter(s)
        for i, char in enumerate(s):
            if char_frequency[char] == 1:
                return i

        return -1


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


    string = "leetcode"
    t.run(s.firstUniqChar(string) == 0)

    string = "loveleetcode"
    t.run(s.firstUniqChar(string) == 2)

    string = 'hihi'
    t.run(s.firstUniqChar(string) == -1)

    string = ''
    t.run(s.firstUniqChar(string) == -1)