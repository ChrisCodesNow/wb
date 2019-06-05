'''
Approach 1:
    Save numeric operations as scores.
    Perform other indicated operations.
    Add all scores

Runtime: O(n)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            if op == '+':
                add = points[-1] + points[-2]
                points.append(add)
            elif op == 'D':
                double = 2 * points[-1]
                points.append(double)
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))
        
        return sum(points)


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

    points = ["5","2","C","D","+"]
    t.run(s.calPoints(points) == 30)

    points = ["5","-2","4","C","D","9","+","+"]
    t.run(s.calPoints(points) == 27)