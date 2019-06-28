'''
Approach 1:
    Compare each word with remaining words:
        Use Counter to check all even indexed chars in word1
        match those in word 2.
        Use Counter to check all odd indexed chars in word1 
        match those in word 2.
        
        If all evens and all odds match, reduce count by 1
        (Initialized to num of words)
        
Runtime: O(m*n^2), for m words of length O(n)
Space Complexity: O(n)


Approach 2:
    Process each word:
        Get all odd characters.
        Get all even characters.
        Sort odd and even characters.
        
        Concatenate and save even + odd as a new word.

        Add new word to set, to only count for distinct 
        strings made from the special equivalent constraint.
Runtime: O(m*n*logn)
Space Complexity: O(m * n)
'''
from collections import Counter
from typing import List
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # return self.solution_01(A)
        return self.solution_02(A)


    # ########################################
    # Approach 1
    #
    def solution_01(self, words):
        count = len(words)
        already_grouped = set()
        for i,word_1 in enumerate(words):
            if i in already_grouped:
                continue
            for j,word_2 in enumerate(words[i + 1:]):
                evens_1, odds_1 = self.get_even_odd(word_1)
                evens_2, odds_2 = self.get_even_odd(word_2)
                
                if self.cancel_out(evens_1, evens_2) and \
                    self.cancel_out(odds_1, odds_2):
                    count -= 1
                    already_grouped.add(i)
                    already_grouped.add(i + j + 1)
        
        return count


    def get_even_odd(self, word):
        evens = [char for i,char in enumerate(word) if i % 2 == 0]
        odds = [char for i,char in enumerate(word) if i % 2 != 0]

        return Counter(evens), Counter(odds)


    def cancel_out(self, freq_1, freq_2):
        if not (freq_1 - freq_2) and not (freq_2 - freq_1):
            return True
        else:
            return False


    # ########################################
    # Approach 2
    #
    def solution_02(self, words):
        groups = set()
        for word in words:
            evens, odds = self.get_parity(word)

            evens = sorted(evens)
            odds = sorted(odds)

            word = "".join(evens) + "".join(odds)
            groups.add(word)

        return len(groups)

    
    def get_parity(self, word):
        evens = [char for i,char in enumerate(word) if i % 2 == 0]
        odds = [char for i,char in enumerate(word) if i % 2 != 0]

        return evens, odds


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

    words = ["abcd", "cbad", "bacd"]
    groups = 2
    t.run(s.numSpecialEquivGroups(words) == groups)


    words = ["abc", "cba"]
    groups = 1
    t.run(s.numSpecialEquivGroups(words) == groups)


    words = ["a","b","c","a","c","c"]
    groups = 3
    t.run(s.numSpecialEquivGroups(words) == groups)


    words = ["aa","bb","ab","ba"]
    groups = 4
    t.run(s.numSpecialEquivGroups(words) == groups)


    words = ["abc","acb","bac","bca","cab","cba"]
    groups = 3
    t.run(s.numSpecialEquivGroups(words) == groups)


    words = ["abcd","cdab","adcb","cbad"]
    groups = 1
    t.run(s.numSpecialEquivGroups(words) == groups)