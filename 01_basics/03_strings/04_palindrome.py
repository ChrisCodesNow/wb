'''
Approach 1:
    Only keep alphanumeric numbers, ignore cases. Then compare front to back.

Approach 2:
    Same as approach 1, but use built in functions and methods

Runtime: O(n)
Space Complexity: O(n), filtered string
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.solution_01(s)
        # return self.solution_02(s)


    def solution_01(self, s):
        if not s:
            return True

        word = self.filter_alnums_01(s)
        word = word.lower()
        return self.palindrome_word_01(word)


    def solution_02(self, s):
        if not s:
            return True

        word = self.filter_alnums_02(s)
        word = word.lower()
        return self.palindrome_word_02(word)


    # Runtime: O(n)
    # Space: O(1)
    def filter_alnums_01(self, sentence):
        word = ""
        for char in sentence:
            if char.isalnum():
                word += char

        return word

    # Runtime: O(n)
    # Space: O(n)
    def filter_alnums_02(self, sentence):
        word = ''.join(list(filter(str.isalnum, sentence)))
        return word

    # Runtime: O(n)
    # Space: O(1)
    def palindrome_word_01(self, word):
        front = 0
        back = len(word) - 1

        while front < back:
            if word[front] != word[back]:
                return False

            front += 1
            back -= 1

        return True

    # Runtime: O(n)
    # Space: O(n)
    def palindrome_word_02(self, word):
        return word == word[::-1]


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

    sentence = "A man, a plan, a canal: Panama"
    t.run(s.isPalindrome(sentence) == True)

    sentence = "race a car"
    t.run(s.isPalindrome(sentence) == False)

    sentence = ""
    t.run(s.isPalindrome(sentence) == True)