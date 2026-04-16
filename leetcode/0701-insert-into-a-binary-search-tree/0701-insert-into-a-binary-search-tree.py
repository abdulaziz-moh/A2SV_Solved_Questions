# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        node = root
        newnode = TreeNode(val)
        while True:
            if not node:
                root = newnode
                break
            if val < node.val:
                if not node.left:
                    node.left = newnode
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = newnode
                    break
                else:
                    node = node.right
        return root