# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root) -> int:
            if not root:
                return 0

            left_height = getHeight(root.left)
            right_height = getHeight(root.right)

            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1

            return max(left_height, right_height) + 1

        return getHeight(root) != -1
