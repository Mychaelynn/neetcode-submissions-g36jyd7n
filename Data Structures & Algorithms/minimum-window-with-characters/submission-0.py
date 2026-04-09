class Solution:
        def minWindow(self, s: str, t: str) -> str:
             resPointers = [-1,-1]             
             length = 0

             sList = list(s)
             have, need = 0, 0
            
             hashNeed, hashS ={}, {}
             
             resLen = float("infinity")

             left=0

             if t == "": return ""

             for c in t:
                hashNeed[c] = 1 + hashNeed.get(c,0)

             need = len(hashNeed)

             for r in range (len(s)):

                currChar = s[r]
                hashS[currChar] = 1 + hashS.get(currChar, 0)

                if currChar in hashNeed and hashS[currChar] == hashNeed[currChar]:
                    have +=1
                
                while have == need:
                    if r - left +1 < resLen:
                        resLen = r - left+1
                        resPointers = [left, r]
                    # pop from left
                    hashS[s[left]] -=1
                    if s[left] in hashNeed and hashS[s[left]] <hashNeed[s[left]]: 
                        have -=1
                    left +=1
            
             l,r = resPointers
             return s[l:r+1] if resLen!= float("infinity") else ""

                


