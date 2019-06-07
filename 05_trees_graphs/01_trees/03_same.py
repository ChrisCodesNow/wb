'''
Approach 1:
    Get and compare preorder structure of trees
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preord_struc(p) == self.preord_struc(q)


    def preord_struc(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        elif not root.left:
            return [root.val, None] + self.preord_struc(root.right)
        else:
            # Don't need to check for absent right subtree
            return [root.val] + self.preord_struc(root.left) + \
                    self.preord_struc(root.right)


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