class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashS1 = dict()
        hashS2 = dict()

        for n in s:
            hashS1[n] = hashS1.get(n, 0) +1

        for n in t:
             hashS2[n] = hashS2.get(n, 0) +1

        if hashS1==hashS2:
            return True
        return False
        