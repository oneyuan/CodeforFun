class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        flag = 1
        r_begin = 0
        r_end = m
        c_begin = 0
        c_end = n
        while r_begin < r_end and c_begin < c_end:
            if flag == 1:
                for i in range(c_begin, c_end):
                    res.append(matrix[r_begin][i])
                flag = 2
                r_begin += 1
            elif flag == 2:
                for i in range(r_begin, r_end):
                    res.append(matrix[i][c_end-1])
                flag = 3
                c_end -= 1
            elif flag == 3:
                for i in range(c_end-1, c_begin-1, -1):
                    res.append(matrix[r_end-1][i])
                flag = 4
                r_end -= 1
            else:
                for i in range(r_end-1, r_begin-1, -1):
                    res.append(matrix[i][c_begin])
                flag = 1
                c_begin += 1
        return res
    
    def spiralOrder0(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        n, m = len(matrix[0]), len(matrix)

        inc = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        step = [n, m-1]
        d = 0
        i, j = 0, -1
        ret = []
        while step[d % 2]:
            for _ in range(step[d % 2]):
                i += inc[d][0]
                j += inc[d][1]
                ret.append(matrix[i][j])
            step[d%2] -= 1
            d = (d+1) % 4
        return ret