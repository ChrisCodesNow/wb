'''
Approach 1:
    Construct char count of each word, determine equality.

Approach 2:
    Same as approach 1, but use built in data structure

Approach 3:
    Use 1 hash table, count chars with s, then reduce chars with t

Runtime: O(n)
Space Complexity: O(n)
'''
from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.solution_01(s, t)
        # return self.solution_02(s, t)
        return self.solution_03(s, t)


    def solution_01(self, s, t):
        char_count_s = self.count_chars(s)
        char_count_t = self.count_chars(t)

        return char_count_s == char_count_t


    def solution_02(self, s, t):
        char_count_s = Counter(s)
        char_count_t = Counter(t)

        return char_count_s == char_count_t


    def solution_03(self, s, t):
        char_count_s = Counter(s)
        return self.same_chars(char_count_s, t)

    
    def count_chars(self, word):
        char_count = defaultdict(int)

        for char in word:
            char_count[char] += 1

        return char_count


    def same_chars(self, char_count, word):
        char_count = self.reduce_char_count(char_count, word)
        return all(char_count[key] == 0 for key in char_count)

    
    def reduce_char_count(self, char_count, word):
        for char in word:
            char_count[char] -= 1

        return char_count


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

    word_s = "anagram"
    word_t = "nagaram"
    t.run(s.isAnagram(word_s, word_t) == True)

    word_s = "rat"
    word_t = "car"
    t.run(s.isAnagram(word_s, word_t) == False)

    word_s = ""
    word_t = "car"
    t.run(s.isAnagram(word_s, word_t) == False)

    word_s = "hello"
    word_t = ""
    t.run(s.isAnagram(word_s, word_t) == False)

    word_s = ""
    word_t = ""
    t.run(s.isAnagram(word_s, word_t) == True)