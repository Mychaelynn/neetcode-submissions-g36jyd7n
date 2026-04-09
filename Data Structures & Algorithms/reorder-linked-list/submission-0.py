class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # 1. Get length (Your logic)
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        # 2. Your 'interleave' logic
        curr_front = head
        # We only need to move (length-1)/2 nodes to the front
        for _ in range((length - 1) // 2):
            
            # --- FIND THE LAST AND SECOND-TO-LAST NODES ---
            # We need the second-to-last to sever the connection
            prev_tail = curr_front
            while prev_tail.next.next:
                prev_tail = prev_tail.next
            
            tail = prev_tail.next
            
            # --- THE MOVE ---
            # A) Sever the old tail
            prev_tail.next = None
            
            # B) Insert tail between curr_front and curr_front.next
            tail.next = curr_front.next
            curr_front.next = tail
            
            # C) Move curr_front forward by two (skip the one we just inserted)
            curr_front = tail.next