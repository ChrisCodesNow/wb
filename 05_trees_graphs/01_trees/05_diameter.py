'''
Approach 1:
    Base:
        Leaf => Diameter = 0, Height = 0.
    Recursive:
        Calculate current diameter = (left + right heights) + 2
        Calculate current height = largest of (left or right heights) + 1
        Update global best diameter


Approach 2:
    Same as approach 1, but use local rather than class variable.
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.solution_01(root)
        return self.solution_02(root)
    
    
    # ########################################
    # Approach 1
    #
    best_diameter = 0
    def solution_01(self, root):
        if root:
            self.get_height(root)

        return self.best_diameter


    def get_height(self, root):
        if not root:
            return -1
        elif not root.left and not root.right:
            return 0
        else:
            left_height = self.get_height(root.left)
            right_height = self.get_height(root.right)
            height = max(left_height, right_height) + 1
            diameter = left_height + right_height + 2

            self.best_diameter = max(self.best_diameter, diameter)
            return height


    # ########################################
    # Approach 2
    #
    def solution_02(self, root):
        best_diameter = [0]
        if root:
            self.get_height_02(root, best_diameter)

        return best_diameter[0]


    def get_height_02(self, root, best_diameter):
        if not root:
            return -1
        elif not root.left and not root.right:
            return 0
        else:
            left_height = self.get_height_02(root.left, best_diameter)
            right_height = self.get_height_02(root.right, best_diameter)
            height = max(left_height, right_height) + 1
            diameter = left_height + right_height + 2

            best_diameter[0] = max(best_diameter[0], diameter)
            return height


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