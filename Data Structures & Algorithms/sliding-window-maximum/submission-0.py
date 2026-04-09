from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Since you imported deque from collections, use deque() directly
        q = deque() 
        output = []
        l, r = 0, 0

        while r < len(nums):
            # 1. Pop smaller values from the back
            # We want to keep the queue in decreasing order
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # 2. ALWAYS add the current index to the queue
            q.append(r)
            
            # 3. Remove the front index if it's no longer in the window
            # Check 'if q' first to avoid errors on the first iteration
            if q and l > q[0]:
                q.popleft()

            # 4. Once the window reaches size k, the max is at the front (q[0])
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
            
        return output