'''
Approach 1:
    Convert to bin, match leading 0's, count bit difference
Runtime: O(b), for b bits
Space Complexity: O(b)

Approach 2:
    Convert to bin with LSB front, count aligned bit complements, count remaining 1's on larger if any
Runtime: O(b), for b bits
Space Complexity: O(b)
'''
from typing import List
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return self.solution_01(x, y)
        return self.solution_02(x, y)


    def solution_01(self, x, y):
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]

        bin_x, bin_y = self.match_leading_zeros(bin_x, bin_y)

        return self.count_bit_complements(bin_x, bin_y)


    def solution_02(self, x, y):
        bin_x = bin(x)[2:][::-1]
        bin_y = bin(y)[2:][::-1]

        count = self.count_aligned_complements(bin_x, bin_y)
        count += self.count_remaining_ones(bin_x, bin_y)

        return count


    # Fill's smaller binary string with leading zeroes, matching string size
    def match_leading_zeros(self, bin_x, bin_y):
        diff = abs(len(bin_x) - len(bin_y))

        if diff:
            if len(bin_x) < len(bin_y):
                bin_x = self.fill_zeros(diff) + bin_x
            else:
                bin_y = self.fill_zeros(diff) + bin_y

        return bin_x, bin_y

    # Make binary string of zeros
    def fill_zeros(self, size):
        return ''.join(['0' for _ in range(size)])


    def count_bit_complements(self, bin_x, bin_y):
        count = 0
        for bit_x,bit_y in zip(bin_x, bin_y):
            if bit_x != bit_y:
                count += 1

        return count


    # Count bit difference on aligned length of bit strings
    def count_aligned_complements(self, bin_x, bin_y):
        count = 0

        mutual_len = min(len(bin_x), len(bin_y))
        for i in range(mutual_len):
            if bin_x[i] != bin_y[i]:
                count += 1

        return count


    # Count 1's on remaining part of longer bit string
    def count_remaining_ones(self, bin_x, bin_y):
        diff = abs(len(bin_x) - len(bin_y))

        if diff:
            if len(bin_x) > len(bin_y):
                return self.count_ones_from(bin_x, len(bin_y))
            else:
                return self.count_ones_from(bin_y, len(bin_x))
        return 0


    def count_ones_from(self, bin_str, i):
        count = 0
        for i in range(i, len(bin_str)):
            if bin_str[i] == '1':
                count += 1

        return count
    
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

    x = 1
    y = 4
    t.run(s.hammingDistance(x, y) == 2)

    x = 0
    y = 0
    t.run(s.hammingDistance(x, y) == 0)

    x = 0
    y = 4
    t.run(s.hammingDistance(x, y) == 1)

    x = 4
    y = 0
    t.run(s.hammingDistance(x, y) == 1)

    x = 4
    y = 1
    t.run(s.hammingDistance(x, y) == 2)

    x = 40
    y = 40
    t.run(s.hammingDistance(x, y) == 0)