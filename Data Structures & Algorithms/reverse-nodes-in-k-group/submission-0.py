# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     curr = head
    #     count = 0
    #     #1 get length
    #     while curr: 
    #         curr = curr.next
    #         count+=1

    #     res = []
    #     curr = head
    #     count2=0

    #     # put k nodes in list and reverse and then connect 
    #     while curr:
    #         resSub = []
    #         if count2+k<count1:
    #             for i in range (k):
    #                 resSub.append(curr)
    #                 curr = curr.next
    #             res.append(reverse(resSub))
    #             count2+=1
    #     for i in range(len(res)-1)
    #         # get tail of each list and attach to head of next 
    # def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head

    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
        

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            groupNext =kth.next

            # reverse
            prev, curr = kth.next, groupPrev.next
            while curr!=groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next  # first node in group --> now last node 
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
            

        
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr



