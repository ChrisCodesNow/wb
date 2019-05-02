'''
Approach 1: 
    All words stacked, one char at time (vertical)
    Size of smallest word
    Find lcp possible among all words

Runtime: O(nw)
Space Complexity: O(n), slicing

Approach 2: 
    2 Adjacent words at a time
    Get lcp at each adjacent word

Runtime: O(nw)
Space Complexity: O(n), slicing
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return self.solution_01(strs)
        return self.solution_02(strs)

    def solution_01(self, words):
        if not words:
            return ''

        common_size = self.smallest_word_size(words)
        for i in range(common_size):
            if not self.same_char_at(words, i):
                return words[0][:i]

        return words[0][:common_size]


    def solution_02(self, words):
        if not words:
            return ''
        lcp_str = words[0]
        for word in words:
            lcp_str = self.adj_lcp(lcp_str, word)
            if lcp_str == '':
                return ''
        
        return lcp_str

    
    def smallest_word_size(self, words):
        min_size = float('inf')
        for word in words:
            min_size = min(min_size, len(word))

        return min_size


    # i comes from smallest_word_size
    def same_char_at(self, words, i):
        char = words[0][i]
        for word in words:
            if word[i] != char:
                return False

        return True


    def adj_lcp(self, word_1, word_2):
        common_size = self.smallest_word_size([word_1, word_2])
        for i in range(common_size):
            if word_1[i] != word_2[i]:
                return word_1[:i]

        return word_1[:common_size]


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

    words = ["flower","flow","flight"]
    t.run(s.longestCommonPrefix(words) == "fl")

    words = ["dog","racecar","car"]
    t.run(s.longestCommonPrefix(words) == "")

    words = ["dog"]
    t.run(s.longestCommonPrefix(words) == "dog")

    words = ["", "dog","racecar",""]
    t.run(s.longestCommonPrefix(words) == "")

    words = ["","",""]
    t.run(s.longestCommonPrefix(words) == "")

    words = []
    t.run(s.longestCommonPrefix(words) == "")