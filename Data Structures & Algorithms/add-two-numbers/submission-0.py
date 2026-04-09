# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1, cur2 = l1, l2

        curr1 = l1
        curr2 = l2
        ten = 1
        num1 = 0
        num2 = 0
        while curr1:
            num1+= curr1.val *ten
            curr1 = curr1.next
            ten*=10

        ten = 1
        while curr2:
            num2+= curr2.val *ten
            curr2 = curr2.next
            ten*=10
    
        sum =  num1+num2


        # now make into a linked list 
        #1 create head
        headRes = ListNode(sum%10)
        currRes = headRes
        sum//=10
        while sum>=1:
            val = sum%10
            currRes.next = ListNode(val)
            currRes = currRes.next
            sum//=10

        return headRes
