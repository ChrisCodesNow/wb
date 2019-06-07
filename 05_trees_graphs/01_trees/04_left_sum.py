'''
Approach :
Runtime: O()
Space Complexity: O()
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.left_sum(root, False)

    
    def left_sum(self, root, from_left):
        if not root:
            return 0
        elif not root.left and not root.right:
            if from_left:
                return root.val
            else:
                return 0
        else:
            return self.left_sum(root.left, True) + \
                    self.left_sum(root.right, False)


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