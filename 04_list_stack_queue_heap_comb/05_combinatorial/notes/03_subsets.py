'''
Approach 1:
    Get subsets of A[0 to n-2]
    Combine each prev subset with current char
Runtime: O()
Space Complexity: O()
'''
def subsets(A):
    if not A:
        return ['']
    else:
        char = A[-1]
        prev_subsets = subsets(A[:len(A) - 1])
        current_subsets = []
        for prev_subset in prev_subsets:
            current_subsets.append(prev_subset + char)

        return prev_subsets + current_subsets


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

    # BUG: returns 2d array
    A = ['1', '2', '3']
    result = subsets(A)
    answer = ['', '1', '2', '3', '12', '13', '23', '123']
    print(sorted(result))
    t.run(sorted(result) == sorted(answer))