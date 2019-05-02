'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from typing import List
class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = bin(num)[2:]
        comp = self.flip_bits(bin_str)
        return int(comp, 2)

    
    def flip_bits(self, bin_str):
        flip_str = ''
        for bit in bin_str:
            flip_str += self.flip_bit(bit)
        
        return flip_str


    def flip_bit(self, bit_char):
        if bit_char == '1':
            return '0'
        else:
            return '1'

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

    num = 5
    t.run(s.findComplement(num) == 2)

    num = 1
    t.run(s.findComplement(num) == 0)

    num = 7
    t.run(s.findComplement(num) == 0)

    num = 12
    t.run(s.findComplement(num) == 3)

