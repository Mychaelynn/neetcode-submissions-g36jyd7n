class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        charArray = list(s)

        left = 0
        right = 1

        uniqueC = set() 

        
        uniqueC.add(charArray[left])
        maxU = 1
        length=1

        while right<len(charArray):
            # add to hashst 
            if charArray[right] in uniqueC:
                uniqueC.remove(charArray[left])
                
                left+=1
                length-=1
            else:
                 uniqueC.add(charArray[right])
                 right+=1
                 length+=1

            
            maxU = max(maxU,length )

        return maxU
                


        