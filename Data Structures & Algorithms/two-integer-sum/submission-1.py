class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = dict()
        index = 0
        for num in nums:
            diff = target - num
            if diff in dict1:
                return [dict1.get(diff), index]
            dict1[num] = index

           

            index += 1

        return 0

        
            
        