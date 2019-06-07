'''
Approach 1:
    Base:
        Leaf => Unival Path = 0, Unival Height = 0
        Empty => Unival Height = 0
    Recursive:
        Calculate current unival height
        Calculate current unival path
        Update best unival path

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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        return self.solution_01(root)


    # ########################################
    # Approach 1
    #
    best_unival_path = 0
    def solution_01(self, root):
        if root:
            self.unival_height_01(root)

        return self.best_unival_path


    def unival_height_01(self, root):
        if not root:
            return -1
        elif not root.left and not root.right:
            return 0
        else:
            left_height = self.unival_height_01(root.left)
            right_height = self.unival_height_01(root.right)

            unival_height = self.get_unival_height(root, left_height, right_height)
            unival_path = self.get_unival_path(root, left_height, right_height)

            self.best_unival_path = max(self.best_unival_path, unival_path)
            return unival_height

    
    def get_unival_height(self, root, left_height, right_height):
        if self.left_right_unipath(root):
            return max(left_height, right_height) + 1
        elif self.left_unipath(root):
            return left_height + 1
        elif self.right_unipath(root):
            return right_height + 1
        else:
            return 0


    def get_unival_path(self, root, left_height, right_height):
        if self.left_right_unipath(root):
            return left_height + right_height + 2
        elif self.left_unipath(root):
            return left_height + 1
        elif self.right_unipath(root):
            return right_height + 1
        else:
            return 0


    def left_right_unipath(self, root):
        if root.left and root.right:
            return root.left.val == root.val and \
                    root.right.val == root.val
        else:
            return False
    

    def left_unipath(self, root):
        if root.left:
            return root.left.val == root.val
        else:
            return False


    def right_unipath(self, root):
        if root.right:
            return root.right.val == root.val
        else:
            return False


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