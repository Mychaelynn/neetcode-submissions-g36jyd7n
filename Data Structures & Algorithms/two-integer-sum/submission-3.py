class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = dict()
        index=0
        for num in nums:
            need = target - num
            if need in dict1:
               
                return [dict1[need], index]

            dict1[num] = index
            index +=1

        
            
        