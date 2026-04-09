class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       if not matrix or not matrix[0]:
        return False
       # binary serach

       length = len(matrix)

       if matrix[length//2][0]>target :
        return self.searchMatrix(matrix[0:length//2],target)
       elif  matrix[length//2][-1]<target:
        return self.searchMatrix(matrix[length//2 +1:],target)
       else:
        currLen = len(matrix[length//2])
        for i in range (currLen):
            if matrix[length//2][i]==target:
                return True
        return False



