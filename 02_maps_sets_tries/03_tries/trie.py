class Node:
    def __init__(self):
        self.is_end_word = False
        self.alphabet = [None for _ in range(26)]

    def set_end_word(self):
        self.is_end_word = True

    def __getitem__(self, idx):
        return self.alphabet[idx]

    def __setitem__(self, idx, child_node):
        self.alphabet[idx] = child_node


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        itr = self.root
        for char in word:
            i = self.idx(char)
            if not itr[i]:
                itr[i] = Node()
            itr = itr[i]

        itr.set_end_word()

    def search(self, word):
        itr = self.root
        for char in word:
            i = self.idx(char)
            if not itr[i]:
                return False
            itr = itr[i]
        
        return itr.is_end_word

    def idx(self, char):
        return ord(char) - ord('a')


if __name__ == "__main__":
    # Test
    class Test:
        count = 0
        def run(self, result):
            self.count += 1
            if result:
                print(f"Passed test {self.count}")
            else:
                print(f"Failed test {self.count}")
    
    
    def make_trie(words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie


    t = Test()

    words_1 = "their the there answer any by bye".split()
    trie = make_trie(words_1)

    words_2 = "hi theire answers anyhow hello zye byes".split()

    in_trie = [word for word in words_1 if trie.search(word)]
    not_in_trie = [word for word in words_2 if not trie.search(word)]

    t.run(sorted(in_trie) == sorted(words_1))
    t.run(sorted(not_in_trie) == sorted(words_2))

