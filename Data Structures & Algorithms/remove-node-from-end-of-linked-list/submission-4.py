# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # figure out len
        curr = head
        curr2 = head
        length=0
        while curr != None:
            length+=1
            curr= curr.next
        
        print(length)
        nodeRemove = length-n
        if length==1:
            return None

        if n==length:
            return head.next


        count2 =0
        while count2!= nodeRemove-1:
            curr2=curr2.next
            count2+=1

        
        temp = curr2.next
        curr2.next = temp.next
        temp.next=None

        return head
            
        