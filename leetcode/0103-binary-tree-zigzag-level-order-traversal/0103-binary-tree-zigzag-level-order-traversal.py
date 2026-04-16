# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root:
            stack = [root]
        else:
            stack = []
        ans, dir = [], True
        while stack:
            arr = stack[:]
            stack, temp = [], []

            if dir:
                for v in arr:
                    temp.append(v.val)
                dir = False
            else:
                for i in range(len(arr)-1, -1, -1):
                    temp.append(arr[i].val)
                dir = True
            ans.append(temp)
            
            for v in arr:
                if v.left:
                    stack.append(v.left)
                if v.right:
                    stack.append(v.right)
        return ans

            
