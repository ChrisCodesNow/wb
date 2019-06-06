'''
Approach 1:
    Base case: 
        n = 0 => Don't create any
    Recursive Case:
        Get balanced parentheses of size n - 1
        Place new balanced parentheses in each spot from prev bal parens.

Runtime: O()
Space Complexity: O()
'''

# Balanced parentheses being generated.
# Thus, only check is all pairs present.
def is_balanced(paren):
    unbalanced_count = 0
    for p in paren:
        if p == '(':
            unbalanced_count += 1
        else:
            unbalanced_count -= 1
    
    return unbalanced_count == 0


def balanced_parens(n):
    if n == 0:
        return ['']
    else:
        prev_balanced = balanced_parens(n - 1)
        curr_balanced = []
        for prev_bal in prev_balanced:
            # Curr balanced have size 1 larger than prev balanced
            for i in range(len(prev_bal) + 1):
                if is_balanced(prev_bal[:i]):
                    paren = '(' + prev_bal[:i] + ')' + prev_bal[i:]
                    curr_balanced.append(paren)
            
        return curr_balanced


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
    t = Test()

    n = 0
    answer = ['']
    output = balanced_parens(n)
    t.run(sorted(answer) == sorted(output))

    n = 1
    answer = ['()']
    output = balanced_parens(n)
    t.run(sorted(answer) == sorted(output))

    n = 2
    answer = ['(())', '()()']
    output = balanced_parens(n)
    t.run(sorted(answer) == sorted(output))

    n = 3
    answer = ["()()()", "()(())", "(())()", "(()())", "((()))"]
    output = balanced_parens(n)
    t.run(sorted(answer) == sorted(output))