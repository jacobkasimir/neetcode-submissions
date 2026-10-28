class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        k = len(matrix[n - 1])
        l = 0
        r = n - 1
        m1 = 0

        while l <= r:
            m = (l+r)//2

            if matrix[m][0] == target or matrix[m][k - 1] == target:
                return True
            elif matrix[m][k - 1] < target:
                l = m + 1
            elif matrix[m][0] > target: 
                r = m - 1
            else:
                l = 0
                r = k - 1
                while l <= r:
                    m1 = (l+r)//2
                    if matrix[m][m1] == target:
                        return True
                    elif matrix[m][m1] < target:
                        l = m1 + 1
                    else:
                        r = m1 - 1

        return True if target == matrix[m][m1] else False