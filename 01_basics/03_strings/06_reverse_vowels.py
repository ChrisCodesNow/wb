'''
Approach 1: 2 Finger Algorithm
    Swap front and back
Runtime: O(n)
Space Complexity: O(1)

Approach 2:
    Get all vowel indices.
    Swap front and back, using indices only


Runtime: O(n)
Space Complexity: O(n)
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        # return self.solution_01(s)
        return self.solution_02(s)


    def solution_01(self, s):
        chars = list(s)
        front = self.next_vowel(s, 0)
        back = self.prev_vowel(s, len(s) - 1)

        while front < back:
            chars[front], chars[back] = chars[back], chars[front]

            front = self.next_vowel(s, front + 1)
            back = self.prev_vowel(s, back - 1)

        return ''.join(chars)


    def solution_02(self, s):
        vowels_indices = self.get_vowel_indices(s)
        return self.swap_chars(s, vowels_indices)

    
    def next_vowel(self, word, front):
        for i in range(front, len(word)):
            if self.is_vowel(word[i]):
                return i

        return len(word)


    def prev_vowel(self, word, back):
        for i in range(back, -1, -1):
            if self.is_vowel(word[i]):
                return i

        return -1


    def get_vowel_indices(self, word):
        indices = []
        for i, char in enumerate(word):
            if self.is_vowel(char):
                indices.append(i)

        return indices

    
    def swap_chars(self, word, indices):
        chars = list(word)
        i = 0
        j = len(indices) - 1
        while i < j:
            front = indices[i]
            back = indices[j]
            chars[front], chars[back] = chars[back], chars[front]

            i += 1
            j -= 1

        return ''.join(chars)
    

    def is_vowel(self, char):
        return char.lower() in set(['a', 'e', 'i', 'o', 'u'])


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


    word = "hello"
    t.run(s.reverseVowels(word) == "holle")

    word = "leetcode"
    t.run(s.reverseVowels(word) == "leotcede")

    word = ""
    t.run(s.reverseVowels(word) == "")

    word = "bcd"
    t.run(s.reverseVowels(word) == "bcd")
