class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        lenArr = len(nums)
        pro = [1] * lenArr
        curr=1
        # going forward
        for i in range(0,lenArr,1):
          pro[i]*=curr
          curr*=nums[i]
           

        # going back 
        curr=1
        for i in range(lenArr-1, -1, -1):
          pro[i]*=curr
          curr*=nums[i]

        return pro


        
       