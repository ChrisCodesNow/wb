'''
Approach 1:

    Base cases:
        1. Empty list
        2. List of size < k


    Get current head and tail
        Stop is group size < k
    Get next head and next tail

    Reverse current group
    Connect reversed tail next tail

Runtime: O(n)
Space Complexity: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        curr_head, curr_tail = self.group_head_tail(head, k)
        if not curr_tail:
            return head

        rev_head = curr_tail
        while curr_tail:
            next_head, next_tail = self.group_head_tail(curr_tail.next, k)
            self.reverse(curr_head, curr_tail)
            rev_tail = curr_head
            if next_tail:
                rev_tail.next = next_tail
            else:
                rev_tail.next = next_head

            curr_head, curr_tail = next_head, next_tail

        return rev_head


    # Guaranteed head node, tail could be a node or NULL
    def group_head_tail(self, head, k):
        itr = head
        count = 0
        while count < k - 1 and itr:
            itr = itr.next
            count += 1

        return head, itr


    # Guaranteed to receive head and tail nodes
    def reverse(self, head, tail):
        stop = tail.next
        prev = None
        curr = head
        while curr != stop:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev


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