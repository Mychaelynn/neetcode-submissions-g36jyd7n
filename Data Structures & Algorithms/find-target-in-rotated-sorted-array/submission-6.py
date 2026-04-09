class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid] : # sorted side
               if target >= nums[l] and target <= nums[mid]: # target in sorted side
                    r = mid - 1
               else: # target in unsorted side
                    l = mid +1
            else: # right side sorted
                if target >= nums[mid] and target <= nums[r]: # in sorted side
                    l = mid + 1
                else:
                    r = mid -1
                
        return -1

            


        