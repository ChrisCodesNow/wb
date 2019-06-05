'''
Approach :
Runtime: O()
Space Complexity: O()
'''
from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = list(Counter(nums).items())
        heapq.heapify(freq)
        pairs = heapq.nlargest(k, freq, key=lambda item:item[1])
        return [pair[0] for pair in pairs]


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

    nums = [1,1,1,2,2,3]
    k = 2
    t.run(s.topKFrequent(nums, k) == [1,2])

    nums = [1]
    k = 1
    t.run(s.topKFrequent(nums, k) == [1])