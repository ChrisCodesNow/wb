'''
Approach 1:
    target = num to add to
    candidates = given list of nums
    selections = list of selected lists
    selected = list of chosen nums from candidate list 
                that add up to num
    total = sum of current selected nums
    start = index of where to start looking
            (avoids duplicated selected such as 
            [2, 2, 3], [3, 2, 2], etc.)
    n = size of candidates


    comb_sum(candidates, target, selections, selected, total, start):
        Base case: total = target 
            => Save current selected
        Iterate candidates on index i [start to n - 1]:
            total + candidates[i] <= target:
                Add candidates[i] to selected
                Recursively comb_sum at start = i, and total = total + candidates[i]
                Remove candidates[i] from selected

        Get all saved selected nums

Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solution_01(candidates, target)


    # ########################################
    # Approach 1
    #
    def solution_01(self, candidates, target):
        selections = []
        selected = self.comb_sum(candidates, target, selections, [], 0, 0)
        return selections


    def comb_sum(self, candidates, target, selections, selected, total, start):
        if total == target:
            selections.append(selected[:])

        for i in range(start, len(candidates)):
            if total + candidates[i] <= target:
                selected.append(candidates[i])
                self.comb_sum(candidates, target, selections, selected, total + candidates[i], i)
                selected.pop()



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
    solution = Solution()
    test = Test()


    candidates = [2,3,6,7]
    target = 7
    result = [
        [7],
        [2,2,3]
    ]
    my_result = solution.combinationSum(candidates, target)
    result = sorted(result)
    my_result = sorted(my_result)
    test.run(result == my_result)

    candidates = [2,3,5]
    target = 8
    result = [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
    my_result = solution.combinationSum(candidates, target)
    result = sorted(result)
    my_result = sorted(my_result)
    test.run(result == my_result)