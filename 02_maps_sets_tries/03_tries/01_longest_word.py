'''
Approach 1:
    Add words to Trie, check largest build word char by char (made up of end words).

Runtime: O(nm), n words of size O(w)
Space Complexity: O(alphabet * m * n)
'''

class Node:
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None for _ in range(26)]


    def set_end_word(self):
        self.end_of_word = True


class Trie:
    def __init__(self):
        self.root = Node()


    def idx(self, char):
        return ord(char) - ord('a')


    def insert(self, key):
        
        itr = self.root
        prev = None
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                itr.children[i] = Node()

            prev = itr
            itr = itr.children[i]

        # prev.set_end_word()
        itr.set_end_word()


    def search(self, key):
        itr = self.root
        prev = None
        for char in key:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            
            prev = itr
            itr = itr.children[i]

        # return prev.end_word
        return itr.end_of_word


from typing import List
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = self.save_words(words)
        return self.build_longest_word(trie)


    def save_words(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie


    def build_longest_word(self, trie):
        S = [(trie.root, "")]
        longest_word = ""
        while S:
            itr, word = S.pop()
            for i,child in enumerate(itr.children):
                if child and child.end_of_word:
                    current_word = word + self.my_chr(i)    # Use same prefix for all children, but add distinct char
                    longest_word = self.update_longest_word(longest_word, current_word)
                    S.append((child, current_word))

        print(longest_word)
        return longest_word
        


    def update_longest_word(self, longest_word, new_word):
        if len(new_word) > len(longest_word):
            return new_word
        elif len(longest_word) > len(new_word):
            return longest_word
        else:
            return sorted([longest_word, new_word])[0]


    def my_chr(self, i):
        return chr(i + ord('a'))

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

    words = ["w","wo","wor","worl", "world"]
    t.run(s.longestWord(words) == "world")

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    t.run(s.longestWord(words) == "apple")