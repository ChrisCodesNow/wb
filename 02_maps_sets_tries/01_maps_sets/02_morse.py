'''
Approach 1:
    Convert words to morse, count unique representations
Runtime: O(nw), for n words of size O(w)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_words = self.get_morse_words(words)
        return self.count_unique(morse_words)


    # Map word to morse equivalent
    def get_morse_words(self, words):
        morse_words = []
        for word in words:
            morse_words.append(self.to_morse(word))

        return morse_words

    def to_morse(self, word):
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_word = ""
        for char in word:
            idx = ord(char) - ord('a')
            morse_word += alphabet[idx]

        return morse_word
        
    def count_unique(self, words):
        unique_words = set(words)
        return len(unique_words)


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


    words = ["gin", "zen", "gig", "msg"]
    t.run(s.uniqueMorseRepresentations(words) == 2)

    words = ["", "zen", "", ""]
    t.run(s.uniqueMorseRepresentations(words) == 2)

    words = ["", ""]
    t.run(s.uniqueMorseRepresentations(words) == 1)

    words = ["hi"]
    t.run(s.uniqueMorseRepresentations(words) == 1)