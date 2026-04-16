# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def findmax(root, mn, mx):
            nonlocal ans
            if not root:
                return
            mn = min(mn, root.val)
            mx = max(mx, root.val)
            ans = max(ans, abs(mx - mn))
            findmax(root.left, mn, mx)
            findmax(root.right, mn, mx)
            return
        findmax(root, root.val, root.val)
        return ans
