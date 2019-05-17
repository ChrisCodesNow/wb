'''
Approach 1:
    At each day either:
    * Haven't bought: Buy at day i or buy later, picking largest profit
    * Already bought: Sell at day i or sell later, picking largest profit (largest sell available)
Runtime: O(TBD)
Space Complexity: O(TBD)

'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solution_01(prices)


    def solution_01(self, prices):
        if len(prices) < 2:
            return 0

        return self.max_profit_r(prices, 0, False)


    def max_profit_r(self, prices, day, bought):
        if day == len(prices) - 1:
            if not bought:
                return 0
            else:
                return prices[day]

        if not bought:
            return max(-prices[day] + self.max_profit_r(prices, day+1, True), \
            self.max_profit_r(prices, day+1, False))
        else:
            return max(prices[day], self.max_profit_r(prices, day+1, True))


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


    prices = [7,1,5,3,6,4]
    t.run(s.maxProfit(prices) == 5)

    prices = [7,6,4,3,1]
    t.run(s.maxProfit(prices) == 0)