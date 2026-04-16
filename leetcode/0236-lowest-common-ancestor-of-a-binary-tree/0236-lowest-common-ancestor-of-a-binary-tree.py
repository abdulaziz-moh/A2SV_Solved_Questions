# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = 0
        def findpq(root):
            nonlocal ans
            if not root:
                return []

            left = findpq(root.left)
            right = findpq(root.right)

            me = []
            if root == p or root == q:
                me = [root.val]

            retval = left + right + me

            if len(retval) == 2:
                ans = root
                return []

            return retval

        findpq(root)
        return ans