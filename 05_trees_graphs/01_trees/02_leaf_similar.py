'''
Approach 1:
    Base:
        1. Empty tree => []
        2. Leaf => Save leaf
    Recursive:
        Get leaf sequences from left and right

Runtime: O(n)
Space Complexity: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_sequence(root1) == self.leaf_sequence(root2)


    def leaf_sequence(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            return self.leaf_sequence(root.left) + \
                    self.leaf_sequence(root.right)

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