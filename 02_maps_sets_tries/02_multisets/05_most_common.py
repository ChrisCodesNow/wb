'''
Approach 1:
    Get paragraph without punctuation, sort by frequency, get top unbanned word

Approach 2:
    Same as approach 1, but remove banned words first, thus sorting a smaller list

Runtime: O(nlogn + nw) for n words in paragraph of size O(w)
Space Complexity: O(n + w)
'''
from collections import Counter
from typing import List
class Solution:

    #
    # Simplify naming of variables
    #
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # return self.solution_01(paragraph, banned)
        return self.solution_02(paragraph, banned)


    def solution_01(self, paragraph, banned):
        paragraph_words = self.separate_words(paragraph)
        paragraph_words = self.remove_punctuation(paragraph_words)
        words_frequency = Counter(paragraph_words)
        return self.top_unbanned_word(words_frequency, set(banned))


    def solution_02(self, paragraph, banned):
        paragraph_words = self.separate_words(paragraph)
        paragraph_words = self.remove_punctuation(paragraph_words)
        clean_words = self.get_clean_words(paragraph_words, set(banned))
        words_frequency = Counter(clean_words)
        return Counter(words_frequency).most_common(1)[0][0]


    def separate_words(self, paragraph):
        paragraph = paragraph.lower().replace(',', ' ')
        return paragraph.split()
        
        
    def get_clean_words(self, words, banned):
        clean_words = list(filter(lambda word: word not in banned, words))

        return clean_words

    def remove_punctuation(self, words_list):
        return list(map(self.simple_word, words_list))


    # Word without punction
    def simple_word(self, word):
        new_word = ''
        for char in word:
            if char.isalnum():
                new_word += char

        return new_word


    def top_unbanned_word(self, words_frequency, banned):
        sorted_words = sorted(words_frequency.items(), key=lambda freq: freq[1], reverse=True)
        for word,count in sorted_words:
            if word not in banned:
                return word


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


    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    t.run(s.mostCommonWord(paragraph, banned) == "ball")


    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    t.run(s.mostCommonWord(paragraph, banned) == "b")


    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    t.run(s.mostCommonWord(paragraph, banned) == "ball")