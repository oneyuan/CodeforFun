class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
                
    def setZeroes0(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows_cnt = len(matrix)
        col_cnt = len(matrix[0])
        zero_rows, zero_cols = set(), set()
        for row_i, row in enumerate(matrix):
            for col_i, col in enumerate(row):
                if not col:
                    zero_rows.add(row_i)
                    zero_cols.add(col_i)
        for row_i in range(rows_cnt):
            if row_i in zero_rows:
                matrix[row_i] = [0] * col_cnt
                continue
            for col_i in range(col_cnt):
                if col_i in zero_cols:
                    matrix[row_i][col_i] = 0       
        