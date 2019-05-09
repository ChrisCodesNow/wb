'''
Approach 1:
    Build char mapping, validate mapping for correctness and one to one

Approach 2:
    Same as approach 1, but use built in functions and dict comprehention

Runtime: O(n)
Space Complexity: O(n)
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return self.solution_01(s, t)
        return self.solution_02(s, t)


    def solution_01(self, s, t):
        map_s = self.get_char_mapping_01(s, t)
        return self.validate_mapping_01(s, t, map_s)


    def solution_02(self, s, t):
        map_s = self.get_char_mapping_02(s, t)
        return self.validate_mapping_02(s, t, map_s)


    # Mapping from s to t
    def get_char_mapping_01(self, s, t):
        mapping = dict()
        for char_s, char_t in zip(s, t):
            mapping[char_s] = char_t

        return mapping


    def get_char_mapping_02(self, s, t):
        mapping = {char_s: char_t for char_s, char_t in zip(s, t)}
        return mapping

    
    # Mapping from s to t
    def validate_mapping_01(self, s, t, map_s):
        if self.duplicate_mapping(map_s):
            return False

        for char_s, char_t in zip(s, t):
            if map_s[char_s] != char_t:
                return False

        return True


    def validate_mapping_02(self, s, t, map_s):
        if self.duplicate_mapping(map_s):
            return False

        return all(map_s[char_s] == char_t for char_s, char_t in zip(s, t))


    # dict -> bool
    # Check for multiple keys going to same value
    def duplicate_mapping(self, map_s):
        seen_chars = set()
        for char in map_s.values():
            if char in seen_chars:
                return True
            seen_chars.add(char)

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

    str_s = "egg"
    str_t = "add"
    t.run(s.isIsomorphic(str_s, str_t) == True)

    str_s = "foo"
    str_t = "bar"
    t.run(s.isIsomorphic(str_s, str_t) == False)

    str_s = "paper"
    str_t = "title"
    t.run(s.isIsomorphic(str_s, str_t) == True)

    str_s = "aaa"
    str_t = "who"
    t.run(s.isIsomorphic(str_s, str_t) == False)

    str_s = "hi"
    str_t = "aa"
    t.run(s.isIsomorphic(str_s, str_t) == False)