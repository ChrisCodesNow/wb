'''
Approach 1:
    Save words in trie, do modified bfs with trie searching prefix until word is found
    Similar to 01(one char at time) and 02(prefix search)

Runtime: O()
Space Complexity: O()
'''
class Node:
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = [None for _ in range(26)]


    def set_end_word(self):
        self.end_of_word = True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        itr = self.root
        for char in word:
            i = self.idx(char)
            if not itr.children[i]:
                itr.children[i] = Node()
            itr = itr.children[i]

        itr.set_end_word()


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        itr = self.root
        for char in word:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            itr = itr.children[i]

        return itr.end_of_word
        

    def starts_with(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        itr = self.root
        for char in prefix:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            itr = itr.children[i]

        return True
        

    def idx(self, char):
        return ord(char) - ord('a')


from collections import deque
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.make_trie(words)
        words_found =  self.words_in_board(board, words, trie)
        return words_found

    def make_trie(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie


    def words_in_board(self, board, words, trie):
        found_words = []
        for word in words:
            indices = self.word_instances(board, word)
            if indices:
                if self.word_in_board(board, word, trie, indices):
                    found_words.append(word)

        return found_words


    # Get coordinates of possible start of word in board
    def word_instances(self, board, word):
        indices = []
        for i,row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    indices.append((i, j))

        return indices


    # Perform bfs on every possible start index of the word in the board
    def word_in_board(self, board, word, trie, indices):
        for u in indices:
            if self.modified_bfs(board, word, trie, u):
                return True

        return False


    # Determine if input word is on the board, 
    # staring with src node.
    # Use trie for quick word search.
    def modified_bfs(self, board, word, trie, src):
        Q = deque()
        Q.append((src, word[0], set([src])))        # Bug 1 solved: Make sure to add initial character

        while Q:
            if word == "aaab" and src == (0, 0):
                print(Q)
            u, current_word, visited = Q.popleft()
            if word == "aaab" and src == (0, 0):
                print(f'id visited = {id(visited)}')
            if word == current_word and trie.search(current_word):       # Bug 2 solved: Check current word, and only add neighbors.
            # Bug 3 solved: Check the actual word is found, and not current build word
                return True

            # Bug 4: I have a single set for the entire bfs, but it should 
            # be distinct sets of visited, one per path being built.
            # FIx at home!
            for v in self.get_neighbors(u, board):
                if v not in visited:
                    i_v, j_v = v
                    adjacent_word = current_word + board[i_v][j_v]
                    visited.add(v)

                    if trie.starts_with(adjacent_word):
                        Q.append((v, adjacent_word, visited))


        return False


    def get_neighbors(self, u, board):
        i, j = u
        m, n = len(board), len(board[0])
        
        if 0 <= i - 1:
            yield (i -1, j)
        if i + 1 < m:
            yield (i + 1, j)
        if 0 <= j - 1:
            yield (i, j - 1)
        if j + 1 < n:
            yield (i, j + 1)


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

    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    t.run(sorted(s.findWords(board, words)) == sorted(["eat","oath"]))

    words = ["oath","pea","eat","rain", "hi"]
    t.run(sorted(s.findWords(board, words)) == sorted(["eat","oath", "hi"]))


    board = [["a"]]
    words = ["a"]
    t.run(sorted(s.findWords(board, words)) == sorted(["a"]))   # My answer = []


    board = [["a","b"],["c","d"]]
    words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
    t.run(sorted(s.findWords(board, words)) == sorted(["ab","ac","bd","ca","db"]))

    board = [["a","b"],["a","a"]]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    t.run(sorted(s.findWords(board, words)) == sorted(["aaa","aaab","aaba","aba","baa"]))
    print(sorted(s.findWords(board, words)))
    # got: ["aba","baa","aaab","aaa","aaaa","aaba"]