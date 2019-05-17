'''
Approach 1:
    At each day either:
    * Haven't bought: Buy at day i or buy later, picking largest profit
    * Already bought: Sell at day i or sell later, picking largest profit (largest sell available)
Runtime: O(n^2)
Space Complexity: O(TBD)

Approach 2:
    Same as approach 1, but memoize largest sell available at each day i, 
    avoiding repeated work.
Runtime: O(n)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.solution_01(prices)
        return self.solution_02(prices)


    # ########################################
    # Approach 1
    #
    def solution_01(self, prices):
        if len(prices) < 2:
            return 0

        return self.max_profit(prices, 0, False)


    def max_profit(self, prices, day, bought):
        if day == len(prices) - 1:
            if not bought:
                return 0
            else:
                return prices[day]

        if not bought:
            return max(-prices[day] + self.max_profit(prices, day+1, True), \
            self.max_profit(prices, day+1, False))
        else:
            return max(prices[day], self.max_profit(prices, day+1, True))


    # ########################################
    # Approach 2
    #
    def solution_02(self, prices):
        if len(prices) < 2:
            return 0

        best_sell = dict()
        return self.max_profit_02(prices, 0, False, best_sell)


    def max_profit_02(self, prices, day, bought, best_sell):
        if day == len(prices) - 1:
            if not bought:
                return 0
            else:
                return prices[day]

        if not bought:
            return max(-prices[day] + self.max_profit_02(prices, day + 1, True, best_sell), \
                        self.max_profit_02(prices, day + 1, False, best_sell))
        elif bought:
            if day not in best_sell:
                best_sell[day] = max(prices[day], \
                                    self.max_profit_02(prices, day + 1, True, best_sell))

            return best_sell[day]

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