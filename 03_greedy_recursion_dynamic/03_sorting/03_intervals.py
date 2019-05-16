'''
Approach 1:
    Sort intervals by start value
    Merge overlaping intervals (inclusive)

    Edge case: No intervals => Stop

Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda interval: interval[0])
        merged_intervals = []
        current_overlap = intervals[0][:]

        for interval in intervals:
            if self.overlap(current_overlap, interval):
                current_overlap = self.join(current_overlap, interval)
            else:
                merged_intervals.append(current_overlap)
                current_overlap = interval[:]

        # Save last overlapping intervals
        merged_intervals.append(current_overlap)
        return merged_intervals


    # Interval 1 has smaller start value than interval 2
    def overlap(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2

        return start_1 <= start_2 and start_2 <= end_1


    # Expand overlaping intervals as wide as possible
    def join(self, interval_1, interval_2):
        start_1, end_1 = interval_1
        start_2, end_2 = interval_2

        start = min(start_1, start_2)
        end = max(end_1, end_2)

        return [start, end]


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


    intervals = [[1,3],[2,6],[8,10],[15,18]]
    t.run(s.merge(intervals) == [[1,6],[8,10],[15,18]])

    intervals = [[1,4],[4,5]]
    t.run(s.merge(intervals) == [[1,5]])

    intervals = []
    t.run(s.merge(intervals) == [])

    intervals = [[1,4],[0,4]]
    t.run(s.merge(intervals) == [[0,4]])