# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfwau

        pointF = head.next
        pointerS = head

        while pointF and pointF.next:
            pointF = pointF.next.next
            pointerS = pointerS.next
        
        # pointS is now middle

        #reverse second half 
        second = pointerS.next
        pointerS.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp


        second = prev
        first = head

        while second!=None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first =temp1
            second = temp2
