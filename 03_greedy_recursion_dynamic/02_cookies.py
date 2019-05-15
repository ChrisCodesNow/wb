'''
Approach 1:
    Align cookies and children in ascending order.
    Give smallest possible cookie to each child
Runtime: O(nlogn)
Space Complexity: O(1)
'''
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        cookies = sorted(s)
        greed_itr = 0
        cookie_itr = 0
        count = 0
        while greed_itr < len(children) and cookie_itr < len(cookies):
            cookie = cookies[cookie_itr]
            greed = children[greed_itr]
            if self.cookie_satisfies_greed(cookie, greed):
                count += 1
                greed_itr += 1
            cookie_itr += 1

        return count


    def cookie_satisfies_greed(self, cookie, greed):
        return cookie >= greed


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


    children = [1,2,3]
    cookies = [1,1]
    t.run(s.findContentChildren(children, cookies) == 1)


children = [1,2]
cookies = [1,2,3]
t.run(s.findContentChildren(children, cookies) == 2)