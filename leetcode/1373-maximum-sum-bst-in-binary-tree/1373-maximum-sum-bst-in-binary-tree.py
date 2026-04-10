# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None, isvalid=False):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
            ans = 0
            def findmax(root):
                if not root:
                    return
                nonlocal ans
                if root and not root.left and not root.right:
                    ans = max(ans, root.val)
                    return (root.val, root.val, True, root.val)

                elif root and not root.left:
                    mnr, mxr, status_r, sm_r = findmax(root.right)
                    if status_r and mnr > root.val:
                        newsum = sm_r + root.val
                        ans = max(ans, newsum)
                        return (root.val, mxr, True, newsum)
                    return (root.val, root.val, False, 0)

                elif root and not root.right:
                    mnl, mxl, status_l, sm_l = findmax(root.left)
                    if status_l and mxl < root.val:
                        newsum = sm_l + root.val
                        ans = max(ans, newsum)
                        return (mnl, root.val, True, newsum)
                    return (root.val, root.val, False, 0)
                    

                mnl, mxl, status_l, sm_l = findmax(root.left)
                mnr, mxr, status_r, sm_r = findmax(root.right)
                if not (status_l and status_r):
                    return (mnl, mxl, False, sm_l)
                if mxl < root.val and mnr > root.val:
                    newsum = root.val + sm_l + sm_r
                    ans = max(ans, newsum)
                    return (mnl, mxr, True, newsum)
                else:
                    return (mnl, mxl, False, sm_l)
            findmax(root)
            return ans