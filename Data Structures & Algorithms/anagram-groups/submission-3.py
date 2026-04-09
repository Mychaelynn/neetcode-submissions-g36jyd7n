from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list) 
        # (tuple (can be anything), list)

        for word in strs:
         
            dict1[tuple(sorted(word))].append(word)

        return list(dict1.values())
        
   
        
