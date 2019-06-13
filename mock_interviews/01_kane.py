# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
(tree) -> (list nodes)
Level Wise Traversal: BFS
    At each levle, get right most node

RT: O(n)
SC: O(n)
'''
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        Q = deque([(root, 0)])
        view = []
        while Q:
            curr,level = Q.popleft()
            if curr.left:
                Q.append((curr.left, level + 1))
            if curr.right:
                Q.append((curr.right, level + 1))

            if level != Q[0][1]:
                view.append(curr)

        return view