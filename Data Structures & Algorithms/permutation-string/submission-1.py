from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)==0:
            return True

        if len(s2)<len(s1):
            return False

        windowSize = len(s1)
        left = 0
        right = windowSize

        # print(text[0:6])

        while right<=len(s2):
            if sorted(s2[left:right]) == sorted(s1):
                return True
            left+=1
            right+=1
        return False




        