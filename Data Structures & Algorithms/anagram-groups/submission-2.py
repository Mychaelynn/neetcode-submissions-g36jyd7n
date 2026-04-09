from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list) 
        # (tuple (can be anything), list)

        for word in strs:
            #making the key
            # sorted returns a list of the characters in a List
            sortedWord = tuple(sorted(word))

            # adding the word to the list of the sorted tuple
            dict1[sortedWord].append(word)

        return list(dict1.values())
        
   
        
