class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #    if not matrix or not matrix[0]:
    #     return False
       # binary serach

    #    length = len(matrix)

    #    if matrix[length//2][0]>target :
    #     return self.searchMatrix(matrix[0:length//2],target)
    #    elif  matrix[length//2][-1]<target:
    #     return self.searchMatrix(matrix[length//2 +1:],target)
    #    else:
    #     currLen = len(matrix[length//2])
    #     for i in range (currLen):
    #         if matrix[length//2][i]==target:
    #             return True
    #     return False


    # Solve with pointers and while loop
        r,c = len(matrix), len(matrix[0])

        top,bot = 0, r-1

        while top<=bot:
            mid = (top+bot)//2
            if matrix[mid][0]>target:
                bot = mid-1
            elif matrix[mid][-1]<target:
                top = mid+1
            else:
                break
        
        if not (top<= bot):
            return False
        else:
            row = (top+bot)//2
            col = len(matrix[row])
            l,r = 0, col-1
            while l<=r:
                mid = (l+r)//2
                if matrix[row][mid]>target:
                    r= mid-1
                
                elif matrix[row][mid]<target:
                    l = mid+1
                else:
                    return True
            return False


