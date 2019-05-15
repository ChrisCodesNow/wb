'''
Approach 1:
    Process each bill, check enough cash available
Runtime: O(n)
Space Complexity: O(n)
'''
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.cash = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if self.have_change_for(bill):
                self.process_payment(bill)
            else:
                return False

        return True

    
    # Check change is available
    def have_change_for(self, bill):
        if bill == 5:
            return True
        elif bill == 10:
            return self.cash[5] > 0
        elif bill == 20:
            return (self.cash[10] > 0 and self.cash[5] > 0) \
                    or self.cash[5] > 2

    
    # Process payment, only called when enough cash available
    def process_payment(self, bill):
        if bill == 10:
            self.cash[5] -= 1
        elif bill == 20:
            if self.cash[10] > 0:
                self.cash[10] -= 1
                self.cash[5] -= 1
            else:
                self.cash[5] -= 3

        self.cash[bill] += 1


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
    

    bills = [5,5,5,10,20]
    t.run(s.lemonadeChange(bills) == True)

    bills = [5,5,10]
    t.run(s.lemonadeChange(bills) == True)

    bills = [10,10]
    t.run(s.lemonadeChange(bills) == False)

    bills = [5,5,10,10,20]
    t.run(s.lemonadeChange(bills) == False)