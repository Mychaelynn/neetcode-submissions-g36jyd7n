# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        curr = head
        c = True
        visitedNodes = set()
        #visitedNodes.add(head)
        if not head:
            return False
        while c:
            if curr.next==None:
                return False
            if curr in visitedNodes:
                return True
            visitedNodes.add(curr)
            curr = curr.next


