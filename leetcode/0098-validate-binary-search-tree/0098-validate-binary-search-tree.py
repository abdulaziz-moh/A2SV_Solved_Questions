# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, mn, mx):
            if not root:
                return True
            return mn < root.val < mx and bst(root.left, mn, root.val) and bst(root.right, root.val, mx)
        return bst(root, float('-inf'), float('inf'))
