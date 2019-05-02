'''
Approach 1:
    Keep adding 1 to next from back, as long as there is a carry.
    Add 1 if all digits were 9's
Runtime: O(n)
Space Complexity: O(1)


Approach 2:
    Find first non 9, from back
    Place 1 at first non 9
    Fill with 0's right of first non 9
Runtime: O(n)
Space Complexity: O(n)

Notes: Both approaches effective
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return self.solution_1(digits)
        return self.solution_2(digits)

    def solution_1(self, digits):
        for i, num in reversed(list(enumerate(digits))):
            total = num + 1
            if total == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] += 1
                break

        if carry:
            return [1] + digits
        else:
            return digits


    def solution_2(self, digits):
        idx = self.non_nine_back(digits)

        if idx >= 0:
            digits[idx] += 1
            return digits[:idx + 1] + [0 for _ in range(idx + 1, len(digits))]
        else:
            return [1] + [0 for _ in range(len(digits))]

    # Returns index of first non nine digit from the back
    def non_nine_back(self, nums):
        for i,num in reversed(list(enumerate(nums))):
            if num != 9:
                return i
        
        return -1


        
        



# Test
if __name__ == '__main__':
    s = Solution()

    l = [1,2,3]
    print(s.plusOne(l) == [1,2,4])

    l = [4,3,2,1]
    print(s.plusOne(l) == [4,3,2,2])

    l = [4,3,2,9]
    print(s.plusOne(l) == [4,3,3,0])

    l = [9,9,9,9]
    print(s.plusOne(l) == [1,0,0,0,0])
