'''
Approach 1:
    Count distinct types of candy, grab as many distinct possible candies for person 1

Approach 2:
    Same as approach 1, but use a set instead of a Counter

Runtime: O(n)
Space Complexity: O(n)

Note: Approach 2 is better, as we don't need a Counter
'''
from collections import Counter
from typing import List
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        # return self.solution_01(candies)
        return self.solution_02(candies)

    
    def solution_01(self, candies):
        type_count = Counter(candies)
        return self.largest_variety(candies, type_count)


    def solution_02(self, candies):
        type_count = set(candies)
        return self.largest_variety(candies, type_count)
    
    # Largest possible variety for one person
    def largest_variety(self, candies, type_count):
        candies_per_person = len(candies) // 2
        num_types = len(type_count)

        return min(candies_per_person, num_types)


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


    candies = [1,1,2,2,3,3]
    t.run(s.distributeCandies(candies) == 3)

    candies = [1,1,1,1]
    t.run(s.distributeCandies(candies) == 1)

    candies = [1,2,3,4,5,6]
    t.run(s.distributeCandies(candies) == 3)

    candies = []
    t.run(s.distributeCandies(candies) == 0)

