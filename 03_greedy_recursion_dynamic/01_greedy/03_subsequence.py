'''
Approach 1:
    Check that s can be built from chars of t, keeping t's order
Runtime: O(t)
Space Complexity: O(1)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_itr = 0
        t_itr = 0
        while s_itr < len(s) and t_itr < len(t):
            char_s = s[s_itr]
            char_t = t[t_itr]
            if char_s == char_t:
                s_itr += 1
            
            t_itr += 1

        return s_itr == len(s)


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

    string_s = "abc"
    string_t = "ahbgdc"
    t.run(s.isSubsequence(string_s, string_t) == True)

    string_s = "axc"
    string_t = "ahbgdc"
    t.run(s.isSubsequence(string_s, string_t) == False)

    string_s = "abc"
    string_t = "a"
    t.run(s.isSubsequence(string_s, string_t) == False)