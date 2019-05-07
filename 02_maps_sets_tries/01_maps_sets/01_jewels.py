'''
Approach 1:
    Count stones that are jewels

Approach 2:
    Same as approach 1, but use built in reduce function

Runtime: O(n)
Space Complexity: O(n)
'''
from functools import reduce
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # return self.solution_01(J, S)
        return self.solution_02(J, S)

    
    def solution_01(self, J, S):
        jewels = set(J)

        count = 0
        for stone in S:
            if stone in jewels:
                count += 1

        return count

    
    def solution_02(self, J, S):
        jewels = set(J)
        return reduce(lambda total, stone: total + 1 if stone in jewels else total, \
                    S, 0)


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

    J = "aA"
    S = "aAAbbbb"
    t.run(s.numJewelsInStones(J, S) == 3)

    J = "z"
    S = "ZZ"
    t.run(s.numJewelsInStones(J, S) == 0)

    J = ""
    S = "ZZ"
    t.run(s.numJewelsInStones(J, S) == 0)

    J = "z"
    S = ""
    t.run(s.numJewelsInStones(J, S) == 0)