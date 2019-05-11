'''
Approach 1:
    Get char frequency, find unique char after difference
Runtime: O(n)
Space Complexity: O(n)
'''
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count_s = Counter(s)
        char_count_t = Counter(t)
        difference = char_count_t - char_count_s        # len(t) = len(s) + 1
        added_char = list(difference)[0]                # Guaranted to have extra char only
        return added_char


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

    string_s = "abcd"
    string_t = "abcde"
    t.run(s.findTheDifference(string_s, string_t) == "e")

    string_s = ""
    string_t = "a"
    t.run(s.findTheDifference(string_s, string_t) == "a")