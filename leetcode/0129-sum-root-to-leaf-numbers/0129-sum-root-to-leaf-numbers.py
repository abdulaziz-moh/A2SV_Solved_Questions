# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(node, topnum):
            if not node:
                return
                
            arr = topnum + [str(node.val)]
            if not node.left and not node.right:
                self.ans += int("".join(arr))

            dfs(node.left, arr)
            dfs(node.right, arr)
        
        dfs(root, [])
        return self.ans