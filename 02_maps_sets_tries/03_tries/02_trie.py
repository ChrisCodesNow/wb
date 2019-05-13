'''
Approach :
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
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        itr = self.root
        for char in word:
            i = self.idx(char)
            if not itr.children[i]:
                return False
            itr = itr.children[i]

        return True
        

    def idx(self, char):
        return ord(char) - ord('a')


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


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