'''
Approach 1:
    Get char frequency, build string by frequency
Runtime: O(nlog(n))
Space Complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        return self.build_string_by_frequency(char_count)


    def build_string_by_frequency(self, char_count):
        sorted_char_count = char_count.most_common(len(char_count))
        sorted_str = ''
        for char, count in sorted_char_count:
            sorted_str += char * count

        return sorted_str


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


    string = "tree"
    t.run(s.frequencySort(string) == "eert" or s.frequencySort(string) == "eetr")

    string = "cccaaa"
    t.run(s.frequencySort(string) == "cccaaa" or s.frequencySort(string) =="aaaccc")

    string = "Aabb"
    t.run(s.frequencySort(string) == "bbAa" or s.frequencySort(string) =="bbaA")