'''
Approach 1:
    Base Case: 
        Combinations of size 0 => Empty set
    Recursion:
        Get combinations of size k - 1
        Match elements in set A with elements in previous combination:
            First remove chosen element in A from previous combination
            (Def choose: once an element is taken, it can't be used again!)
Runtime: O()
Space Complexity: O()
'''
def combinations(A, k):
    if k == 0:
        return ['']
    elif k == 1:
        return A[:]
    else:
        prev_combinations = combinations(A, k - 1)
        curr_combinations = []
        for s in A:
            prev_combinations.remove(s)
            for prev_comb in prev_combinations:
                curr_combinations.append(s + prev_comb)

        return curr_combinations


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

    A = ['1', '2', '3', '4']
    k = 2 
    answer = ['12', '13', '14', '23', '24', '34']
    output = combinations(A, k)
    t.run(sorted(answer) == sorted(output))

    
    A = ['1', '2', '3', '4', '5']
    k = 2 
    answer = ['12', '13', '14', '15', '23', '24', '25', '34', '35', '45']
    output = combinations(A, k)
    t.run(sorted(answer) == sorted(output))