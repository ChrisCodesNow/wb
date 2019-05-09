'''
Approach 1:
    Build mapping, validate mapping mathcing and one to one(no duplicate values)
    Edge cases: empty pattern or distinct quantities

Runtime: O(n)
Space Complexity: O(n)
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()

        # Edge case
        if not pattern or len(pattern) != len(str):
            return False

        map_p = self.build_mapping(pattern, str)
        return self.is_bijection(pattern, str, map_p)


    # Mapping pattern to words
    # (str, list str) -> dict
    def build_mapping(self, pattern, words):
        mapping = {char_p: word for char_p, word in zip(pattern, words)}
        return mapping


    # Check for bijection
    # (str, list str, dict) -> bool
    def is_bijection(self, pattern, words, pattern_mapping):
        if self.has_duplicate_values(pattern_mapping):
            return False

        for char_p, word in zip(pattern, words):
            if pattern_mapping[char_p] != word:
                return False

        return True


    # dict -> bool
    def has_duplicate_values(self, mapping):
        seen_values = set()
        for value in mapping.values():
            if value in seen_values:
                return True
            seen_values.add(value)

        return False
    

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


    pattern = "abba"
    words = "dog cat cat dog"
    t.run(s.wordPattern(pattern, words) == True)

    pattern = "abba"
    words = "dog cat cat fish"
    t.run(s.wordPattern(pattern, words) == False)

    pattern = "aaaa"
    words = "dog cat cat dog"
    t.run(s.wordPattern(pattern, words) == False)

    pattern = "abba"
    words = "dog dog dog dog"
    t.run(s.wordPattern(pattern, words) == False)

    pattern = ""
    words = "dog dog dog dog"
    t.run(s.wordPattern(pattern, words) == False)

    pattern = "aaa"
    words = "aa aa aa aa"
    t.run(s.wordPattern(pattern, words) == False)

    
