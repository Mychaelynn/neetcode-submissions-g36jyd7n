class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        left, right = 0,0
        mid = len(matrix)/2

        for arr in matrix:
            maxV = max(arr)
            minV = min(arr)

            if target>=minV and target<=maxV:
                if target in arr:
                    return True
                else:
                    return False

        return False