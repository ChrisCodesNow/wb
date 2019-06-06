'''
Approach 1:
    Get permutations of Subset A1 to An-1
    Place A0 in between each gap in all permutations of Subset A1 to An-1
Runtime: O()
Space Complexity: O()
'''
def set_permutations(A):
    if not A:
        return ['']
    else:
        char = A[0]
        prev_perms = set_permutations(A[1:])
        curr_perms = []
        for perm in prev_perms:
            # Current permuatations size > previous permuatations by 1 char
            for i in range(len(perm) + 1):
                curr_perms.append(perm[:i] + char + perm[i:])
        
        return curr_perms


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

    A = ['1', '2', '3']
    perms = ['123', '132', '213', '231', '312', '321']
    output = set_permutations(A)
    t.run(sorted(output)== sorted(perms))