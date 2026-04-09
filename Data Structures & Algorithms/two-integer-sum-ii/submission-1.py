class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

    
        lenList = len(numbers)

        for i in range(lenList):
            for j in range(i, lenList):
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
                