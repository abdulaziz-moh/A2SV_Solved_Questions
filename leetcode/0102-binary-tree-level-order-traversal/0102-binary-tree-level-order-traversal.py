# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        ans = []
        while queue:
            temp, newqueue = [], deque()
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                temp.append(node.val)
                newqueue.append(node.left)
                newqueue.append(node.right)
            if temp: ans.append(temp)
            queue = newqueue
        return ans

            
