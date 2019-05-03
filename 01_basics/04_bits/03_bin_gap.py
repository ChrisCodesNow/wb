'''
Approach 1:
    Convert num to bin, count largest consecutive one

Approach 2:
    Convert to binary, get indices of ones, calculate largest adjacent difference
    
Runtime: O(b)
Space Complexity: O(b)
'''
class Solution:
    def binaryGap(self, N: int) -> int:
        # return self.solution_01(N)
        return self.solution_02(N)


    def solution_01(self, N):
        bin_str = bin(N)[2:]
        gap = self.largest_gap_ones(bin_str)
        return gap


    def solution_02(self, N):
        bin_str = bin(N)[2:]
        ones_indices = self.get_indices_ones(bin_str)
        return self.max_adjacent_difference(ones_indices)
    

    def largest_gap_ones(self, bin_str):
        gap = 0
        prev_one = None

        for i,bit in enumerate(bin_str):
            if bit == '1':
                if prev_one == None:
                    prev_one = i
                else:
                    gap = max(gap, i - prev_one)
                    prev_one = i

        return gap


    def get_indices_ones(self, bin_str):
        ones_indices = []
        for i,bit in enumerate(bin_str):
            if bit == '1':
                ones_indices.append(i)

        return ones_indices

    
    def max_adjacent_difference(self, indices):
        if len(indices) <= 1:
            return 0

        difference = indices[1] - indices[0]
        for i in range(len(indices) - 1):
            difference = max(difference, indices[i + 1] - indices[i])

        return difference


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

    num = 22
    t.run(s.binaryGap(num) == 2)

    num = 5
    t.run(s.binaryGap(num) == 2)

    num = 6
    t.run(s.binaryGap(num) == 1)

    num = 8
    t.run(s.binaryGap(num) == 0)