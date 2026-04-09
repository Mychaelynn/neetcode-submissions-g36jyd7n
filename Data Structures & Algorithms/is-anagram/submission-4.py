class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        
        for stri in s:
            dict1[stri]+=1

        for stri in t:
            dict2[stri]+=1

        return dict1==dict2