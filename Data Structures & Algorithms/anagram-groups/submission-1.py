from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list) 

        for word in strs:
            sortedWord = tuple(sorted(word))

            dict1[sortedWord].append(word)

        return list(dict1.values())
        
   
        
