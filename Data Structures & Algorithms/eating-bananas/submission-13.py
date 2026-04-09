class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        # if len(piles) == h:
        #     return max(piles)

        # maxV = max(piles)
        # #print(maxV)
        # hours = 0
        # for i in range (1,maxV+1):
        #     hours = 0
        #     for j in range(len(piles)):
        #         hours+= math.ceil(piles[j]/i)

        #     if hours<=h:
        #         return i

        # NOW WITH BINARY SEARCH 

        if len(piles) == h:
            return max(piles)
        maxV = max(piles)
        hours = 0
        l = 1
        r =maxV
        mid = maxV//2
        minV=maxV
        while l<=r :
            mid = (l+r)//2
            hour = 0
            for p in piles:
                hour+= math.ceil(p/mid)
            if hour<=h:
                minV=min(mid,minV)
                r = mid-1
            else:
                l = mid+1
            
        return minV

            
        

        