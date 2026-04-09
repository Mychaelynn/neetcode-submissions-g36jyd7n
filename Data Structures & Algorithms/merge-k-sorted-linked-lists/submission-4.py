# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        amount = len(lists)
        if amount ==0:
            return None
        if amount ==1:
            return lists
        merged = lists[0]

        for i in range (1,amount):
            mergeRes = self.mergeTwoLists(merged,lists[i])
            merged = mergeRes

        return mergeRes
        

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Your logic here

        curr1 = list1
        curr2 = list2

        # start of head
        if curr1.val>curr2.val:
            res = ListNode(curr2.val,None)
            curr2 = curr2.next
        else:   
            res = ListNode(curr1.val, None)
            curr1 = curr1.next
        head = res
        
        while curr1 and curr2:
            if curr1.val<curr2.val:
                res.next = ListNode(curr1.val,None)
                curr1 = curr1.next
            else:
                res.next = ListNode(curr2.val,None)
                curr2 = curr2.next
            res = res.next
        if curr1:
            while curr1:
                res.next = ListNode(curr1.val,None)
                curr1 = curr1.next
                res = res.next
        if curr2:
            while curr2:
                res.next = ListNode(curr2.val,None)
                curr2 = curr2.next
                res = res.next
        return head;
