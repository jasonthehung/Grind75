# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         def dfs(node):
#             if not node:
#                 return 0

#             left_h = dfs(node.left)
#             right_h = dfs(node.right)

#             return max(left_h, right_h) + 1

#         return dfs(root)


# from collections import deque


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         queue = deque([root])
#         depth = 0

#         while queue:
#             level_size = len(queue)

#             for _ in range(level_size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             depth += 1


#         return depth
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        st = [(root, 1)]
        max_d = 0

        while st:
            node, depth = st.pop()
            max_d = max(depth, max_d)

            if node.left:
                st.append((node.left, depth + 1))
            if node.right:
                st.append((node.right, depth + 1))

        return max_d
