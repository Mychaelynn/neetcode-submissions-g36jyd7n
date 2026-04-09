# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        amount = len(lists)
        mergedLists = []
        if amount ==0:
            return None
        if amount ==1:
            return lists
        merged = lists[0]

        while len(lists)>1:
            mergedLists = []

            for i in range (0,len(lists),2):
                l2 = lists[i+1] if i+1<len(lists) else None
                mergeRes = self.mergeTwoLists(lists[i],l2)
                mergedLists.append(mergeRes)
            lists = mergedLists

        return mergeRes


        # merge sort 

        mid 
        

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Your logic here

        curr1 = list1
        curr2 = list2
        
        if not curr1: 
            return curr2
        if not curr2:
            return curr1

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
