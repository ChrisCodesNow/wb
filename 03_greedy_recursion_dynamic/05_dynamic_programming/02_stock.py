'''
Approach 1:
    At each day i either you:
        1. Don't have stock, get max profit from:
            1. Buy at day i, sell any day i + 1 to n - 1
            2. Buy any day i + 1 to n - 1
        2. Have stock, get max profit from:
            1. Sell at day i
            2. Sell any day i + 1 to n - 1

    Dynamic Algo: Fill Array
    1.  best_profit = array with best profit per day
        best_sell = array with best sell price possible
    2. Fill base cases:
        best_profit[last day] = 0
        best_sell[last day] = price[last day]
    3. Fill arary:
        Compute best profit and update best sell

Runtime: O(n)
Space Complexity: O(n)

Approach 2:
    Same as approach 1, bottom up approach but only save solution to 
    previous subproblem i + 1 that will help compute current subproblem i
Runtime: O(n)
Space Complexity: O(1)
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
        n = len(prices)
        if n < 2:
            return 0

        best_profit = [0 for _ in range(n)]
        best_sell = prices[:]

        for i in range(n - 2, -1, -1):
            best_profit[i] = max(-prices[i] + best_sell[i + 1], 
                                best_profit[i + 1])
            best_sell[i] = max(best_sell[i], best_sell[i + 1])

        return best_profit[0]


    # ########################################
    # Approach 2
    #
    def solution_02(self, prices):
        n = len(prices)
        if n < 2:
            return 0

        best_profit = 0
        best_sell = prices[-1]

        for i in range(n - 2, -1, -1):
            best_profit = max(-prices[i] + best_sell, 
                            best_profit)
            best_sell = max(prices[i], best_sell)

        return best_profit


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