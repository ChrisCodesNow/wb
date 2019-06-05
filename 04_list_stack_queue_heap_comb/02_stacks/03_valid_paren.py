'''
Approach 1:
    Validate matching pairs or add open parentheses
    Errors when: Missmatch, run out of stack elements, have
Runtime: O()
Space Complexity: O()
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        seen_open = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for paren in s:
            if paren in pairs:
                seen_open.append(paren)
            else:
                if not seen_open:
                    return False
                elif pairs[seen_open[-1]] != paren:
                    return False
                else:
                    seen_open.pop()

        if seen_open:
            return False
        else:
            return True


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


    paren = "()"
    t.run(s.isValid(paren) == True)

    paren = "()[]{}"
    t.run(s.isValid(paren) == True)

    paren = "(]"
    t.run(s.isValid(paren) == False)

    paren = "([)]"
    t.run(s.isValid(paren) == False)

    paren = "{[]}"
    t.run(s.isValid(paren) == True)