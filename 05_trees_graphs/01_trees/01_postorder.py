'''
Approach 1:
    Base:
        Empty tree => []
    Recursive:
        Get postorder of subtrees from left to right
        Get current root node value

Approach 2:
    Add stack top to result
    Add children of current node to stack

Runtime: O(n)
Space Complexity: O(n)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.solution_01(root)
        return self.solution_02(root)


    # ########################################
    # Approach 1
    # Recursive
    def solution_01(self, root):
        if not root:
            return []
        else:
            descendants = []
            for child in root.children:
                descendants += self.solution_01(child)

            return descendants + [root.val]


    # ########################################
    # Approach 2
    # Iterative
    def solution_02(self, root):
        if not root:
            return []
        else:
            s = [root]
            tree_list = []
            while s:
                r = s.pop()
                tree_list.append(r.val)
                for child in r.children:
                    s.append(child)
                
            return tree_list[::-1]


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