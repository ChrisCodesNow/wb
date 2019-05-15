'''
Approach 1:
    Build and countn overlaping intervals
    Sort balloons by start range value
Runtime: O(n)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        balloons = sorted(points, key=lambda coord: coord[0])
        num_arrows = 0
        current_interval = balloons[0][:]

        for balloon in balloons:
            if self.overlap(current_interval, balloon):
                current_interval = self.intersect_intervals(current_interval, balloon)
            else:
                num_arrows += 1
                current_interval = balloon[:]

        # pop last interval
        num_arrows += 1
        return num_arrows

    
    # interval 1 start <=  interval 2
    def overlap(self, interval_1, interval_2):
        s_1, e_1 = interval_1
        s_2 = interval_2[0]

        return s_1 <= s_2 and s_2 <= e_1


    def intersect_intervals(self, interval_1, interval_2):
        s_1, e_1 = interval_1
        s_2, e_2 = interval_2

        start = max(s_1, s_2)
        end = min(e_1, e_2)

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


    balloons = [[10,16], [2,8], [1,6], [7,12]]
    t.run(s.findMinArrowShots(balloons) == 2)
