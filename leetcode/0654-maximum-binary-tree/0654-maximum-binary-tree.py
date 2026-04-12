# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildtree(left, right):
            if left > right:
                return

            mxidx, mxv = left, nums[left]
            for i in range(left, right+1):
                if mxv < nums[i]:
                    mxv = nums[i]
                    mxidx = i

            newnode = TreeNode(mxv)
            newnode.left = buildtree(left, mxidx-1)
            newnode.right = buildtree(mxidx+1, right)
            
            return newnode
        return buildtree(0, len(nums)-1)

            