class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        pointStart = 0
        pal = True
        lowerS = ''.join(c.lower() for c in s if c.isalnum())
        pointEnd = len(lowerS) - 1
        if len(lowerS) == 0 or len(lowerS) == 1:
            return True

        while pal:

            if lowerS[pointStart] == lowerS[pointEnd]:
                pointStart += 1
                pointEnd -= 1

            else:
                return False

            if pointStart >= pointEnd:
                return True
