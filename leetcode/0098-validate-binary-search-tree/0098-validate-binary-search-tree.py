# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isvalid(root, mn, mx):
            if not root:
                return True
            return mn < root.val < mx and isvalid(root.left,mn, root.val) and isvalid(root.right, root.val, mx)
        return isvalid(root, -inf, inf)