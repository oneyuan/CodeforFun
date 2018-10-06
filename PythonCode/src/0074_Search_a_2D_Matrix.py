class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
            if n == 0:
                return False
        else:
            return False
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][n-1] >= target:
                s = 0
                e = n-1
                while s <= e:
                    t = (s+e)//2
                    if matrix[i][t] == target:
                        return True
                    elif matrix[i][t] < target:
                        s = t+1
                    else:
                        e = t-1
        return False
    
    def searchMatrix0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        r_l = 0
        r_h = len(matrix)-1
        
        while r_l < r_h:
            r_m = (r_l+r_h)//2
            if matrix[r_m][0] == target:
                return True
            if target < matrix[r_m][0]:
                r_h = r_m-1
            else:
                r_l = r_m+1
                
        if target < matrix[r_l][0]:
            r = r_l-1
        else:
            r = r_l
        
        if target > matrix[r][-1]:
            return False
        c_l = 0
        c_h = len(matrix[0])-1
        while c_l <= c_h:
            c_m = (c_l+c_h)//2
            if matrix[r][c_m] == target:
                return True
            if matrix[r][c_m] < target:
                c_l = c_m+1
            else:
                c_h = c_m-1
                
        return False