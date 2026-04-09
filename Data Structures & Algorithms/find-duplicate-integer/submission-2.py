class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # diction = set()

        # for i in range (len(nums)):
        #    if nums[i] in diction:
        #     return nums[i]
        #    diction.add(nums[i])
            

        # now solve in O(1) memory

        for i in range (len(nums)):
            val = abs(nums[i])
            if nums[val]<0:
                #print(nums[i])
                return abs(nums[i])
            #print("making index "+str(abs(nums[i])) +"negative")                
            nums[abs(val)] = -nums[val]

        
        