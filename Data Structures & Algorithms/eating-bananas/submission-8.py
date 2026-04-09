import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range: minimum speed is 1, max is the largest pile
        low = 1
        high = max(piles)
        result = high 

        while low <= high:
            k = (low + high) // 2
            total_hours = 0
            
            for p in piles:
                # Ceiling division: how many hours for this pile at speed k?
                total_hours += math.ceil(p / k)
            
            if total_hours <= h:
                # If she finishes in time, k might be the answer, 
                # but let's try even slower (move left)
                result = k
                high = k - 1
            else:
                # Too slow! Must increase speed (move right)
                low = k + 1
                
        return result