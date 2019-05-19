'''
Approach 1:
    At each char i in word1 and char j in word2, either go to 
    the next char if they match or get the smallest from:
    1. Replacing char i with char j
    2. Inserting char j before char i
    3. Deleting char i

    Base Cases:
        1. Reach end of both words: Stop
        2. Reach end of word1: insert remaining chars from word2
        3. Reach end of word2: delete remaining chars from word1

Runtime: O(TBD)
Space Complexity: O(TBD)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.edit_distance_01(word1, word2, 0, 0)


    # ########################################
    # Approach 1
    #
    def edit_distance_01(self, word_1, word_2, i, j):
        if i == len(word_1) and j == len(word_2):
            return 0
        elif i == len(word_1):
            return 1 + self.edit_distance_01(word_1, word_2, i, j + 1)
        elif j == len(word_2):
            return 1 + self.edit_distance_01(word_1, word_2, i + 1, j)

        if word_1[i] == word_2[j]:
            return self.edit_distance_01(word_1, word_2, i + 1, j + 1)
        else:
            return 1 + min(self.edit_distance_01(word_1, word_2, i +1, j + 1),
                        self.edit_distance_01(word_1, word_2, i, j + 1),
                        self.edit_distance_01(word_1, word_2, i + 1, j))


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


    word_1 = "horse"
    word_2 = "ros"
    t.run(s.minDistance(word_1, word_2) == 3)

    word_1 = "intention"
    word_2 = "execution"
    t.run(s.minDistance(word_1, word_2) == 5)