'''
Approach 1:
    Base:
        Leaf from left => Update bottom left to deepest leaf
    Recursive:
        Search for bottom left using post order traversal.
        Track current node's depth

Runtime: O(n)
Space Complexity: O(n)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
# Bottom left object class
class BL:
    def __init__(self, val, x, depth):
        self.val = val
        self.x = x
        self.depth = depth

    
    def update(self, other_bl):
        if other_bl.depth > self.depth or \
            (other_bl.depth == self.depth and other_bl.x < self.x):
            self.val = other_bl.val
            self.x = other_bl.x
            self.depth = other_bl.depth


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        deepest = BL(root.val, 0, 0)
        self.bottom_left(root, 0, 0, False, deepest)
        
        return deepest.val

        
    # ########################################
    # Approach 1
    #
    def bottom_left(self, root, horizontal, depth, from_left, deepest):
        if not root:
            return None
        elif not root.left and not root.right:
            current = BL(root.val, horizontal, depth)
            deepest.update(current)
        else:
            self.bottom_left(root.left, horizontal - 1, depth + 1, True, deepest)
            self.bottom_left(root.right, horizontal + 1, depth + 1, False, deepest)

    

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