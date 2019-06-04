'''
Approach 1:
    Re arrange pointers, reversign order of list
Runtime: O(n)
Space Complexity: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return self.solution_01(head)
        return self.solution_02(None, head)

            
    # Iterative approach
    def solution_01(self, head):
        if not head:
            return head

        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev


    # Recursive approach
    def solution_02(self, prev, curr):
        if not curr:
            return prev
        
        next = curr.next
        curr.next = prev

        return solution_02(curr, next)

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

    head = None
    t.run(s.reverseList(head) == None)
