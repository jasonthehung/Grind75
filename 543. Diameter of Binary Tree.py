# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dfs(node):
            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            self.d = max(self.d, left_h + right_h)

            return max(left_h, right_h) + 1

        dfs(root)

        return self.d
