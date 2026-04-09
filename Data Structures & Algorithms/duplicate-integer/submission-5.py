class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict1 = set()

        for num in nums:
            if num in dict1:
                return True
            dict1.add(num)

        return False