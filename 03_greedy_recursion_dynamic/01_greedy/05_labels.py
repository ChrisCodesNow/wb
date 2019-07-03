'''
Approach 1:
    Get frequency of each character.
    Find group sizes:
        Iterate characters:
            Add character to remaining:
                Remove character from frequency.
            Add 1 to group size.
            Remove 1 from remaining.

            No more remaining:
                Save current group size.
                Reset group size.

Runtime: O(n)
Space Complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_frequency = Counter(S)
        return self.get_group_sizes(S, char_frequency)

    
    def get_group_sizes(self, S, char_frequency):
        group_sizes = []
        size = 0
        remaining = 0
        for char in S:
            if char in char_frequency:
                remaining += char_frequency[char]
                del char_frequency[char]

            size += 1
            remaining -= 1

            if remaining == 0:
                group_sizes.append(size)
                size = 0

        return group_sizes
    # ########################################
    # Approach 1
    #

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


    S = "ababcbacadefegdehijhklij"
    result = [9,7,8]
    my_result = s.partitionLabels(S)

    t.run(result == my_result)