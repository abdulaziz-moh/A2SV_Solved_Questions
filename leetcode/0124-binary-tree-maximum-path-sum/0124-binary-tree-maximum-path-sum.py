# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf

        def bottom_up_dfs(root):
            if not root:
                return 0
            
            left = bottom_up_dfs(root.left)
            right = bottom_up_dfs(root.right)
            left, right = max(0,left), max(0,right)
            self.ans = max(self.ans, left + right + root.val)

            return max(left, right) + root.val
        bottom_up_dfs(root)
        return self.ans