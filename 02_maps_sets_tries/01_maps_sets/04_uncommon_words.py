'''
Approach 1:
    Get unique words, get words in one but not another
Runtime: O(n)
Space Complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        unique_A = self.get_unique_words(A)
        unique_B = self.get_unique_words(B)
        uncommon_words = self.get_uncommon_words(unique_A, B)
        uncommon_words += self.get_uncommon_words(unique_B, A)

        return uncommon_words


    # Extract unique words from list
    # str -> set
    def get_unique_words(self, sentence):
        words = sentence.split()
        words_frequency = Counter(words)
        unique_words = set(word for word in words_frequency if words_frequency[word] == 1)
        return unique_words


    # Unique words not in sentence
    # (str, set) -> List str
    def get_uncommon_words(self, unique_words, sentence):
        sentence_words = set(sentence.split())
        uncommon_words = []
        for word in unique_words:
            if word not in sentence_words:
                uncommon_words.append(word)

        return uncommon_words


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


    A = "this apple is sweet"
    B = "this apple is sour"
    t.run(s.uncommonFromSentences(A, B) == ["sweet","sour"])

    A = "apple apple"
    B = "banana"
    t.run(s.uncommonFromSentences(A, B) == ["banana"])

    A = "apple"
    B = "banana"
    t.run(sorted(s.uncommonFromSentences(A, B)) == sorted(["banana", "apple"]))

    A = "banana"
    B = ""
    t.run(sorted(s.uncommonFromSentences(A, B)) == sorted(["banana"]))

    A = ""
    B = ""
    t.run(sorted(s.uncommonFromSentences(A, B)) == sorted([]))

    A = "apple apple"
    B = "banana banana"
    t.run(s.uncommonFromSentences(A, B) == [])

    A = "apple banana"
    B = "banana apple"
    t.run(s.uncommonFromSentences(A, B) == [])


    A = "s z z z s"
    B = "s z ejt"
    t.run(s.uncommonFromSentences(A, B) == ["ejt"])