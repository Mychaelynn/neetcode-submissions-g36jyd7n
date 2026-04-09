
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s)==0:
            return 0

        
        
        length=0
        left = 0
        right = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)

            while (right-left+1) - max(count.values())>k:
                count[s[left]]-=1
                left+=1
            
            
            length = max(length, right-left+1)
        return length

        