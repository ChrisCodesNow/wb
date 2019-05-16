'''
Approach 1:
    Modified binary search, ,look for peak
Runtime: O(logn)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if self.peak_in_front(A):
            return A[0]
        elif self.peak_in_back(A):
            return A[-1]

        start = 0
        end = len(A) - 1

        # Guaranteed to find peak
        while start <= end:
            mid = (start + end) // 2
            if self.is_increasing(A, mid):
                start = mid + 1
            elif self.is_decreasing(A, mid):
                end = mid - 1
            else:
                return mid


    def peak_in_front(self, A):
        return A[0] > A[1]

    
    def peak_in_back(self, A):
        return A[-1] > A[-2]


    def is_increasing(self, A, i):
        return A[i - 1] < A[i] and A[i] < A[i + 1]

    
    def is_decreasing(self, A, i):
        return A[i - 1] > A[i] and A[i] > A[i + 1]


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


    A = [0,1,0]
    t.run(s.peakIndexInMountainArray(A) == 1)

    A = [0,2,1,0]
    t.run(s.peakIndexInMountainArray(A) == 1)


    A = [0, 1, 2, 2, 3]
    t.run(s.peakIndexInMountainArray(A) == 3)