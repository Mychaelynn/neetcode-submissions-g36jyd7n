class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        numSet = set()
        for num in nums:
            numSet.add(num)
        numSet = sorted(list(numSet))
        print(numSet)

        count = 1
        maxCount=1
        prevNum = numSet[0]
        for i in range (1, len(numSet)):
            if (numSet[i]==prevNum+1):
                count+=1
            else:
                count = 1
            if count>maxCount:
                    maxCount = count
            prevNum = numSet[i]
        return maxCount