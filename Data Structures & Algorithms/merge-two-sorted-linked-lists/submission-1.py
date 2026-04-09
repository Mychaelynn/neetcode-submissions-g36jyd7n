# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr2=list2
        curr1=list1
        ans = ListNode(0)
        ansHead = ans
        while list1 and list2:
            if list1.val<=list2.val:
                ansHead.next=list1
                list1=list1.next
                
            else:
                ansHead.next=list2
                list2=list2.next

            ansHead = ansHead.next
        if list1:
            ansHead.next=list1
        if list2:
            ansHead.next=list2
        return ans.next
                