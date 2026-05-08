# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for llist in lists:
            while llist:
                heappush(heap, llist.val)
                llist = llist.next
        
        ans = None
        temp = ans
        while heap:
            v = heappop(heap)
            newnode = ListNode(v)

            if not ans:
                ans = newnode
                temp = ans
            else:
                temp.next = newnode
                temp = newnode
        return ans
            