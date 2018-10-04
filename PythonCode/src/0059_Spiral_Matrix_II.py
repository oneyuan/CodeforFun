class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        r_begin = 0
        r_end = n
        c_begin = 0
        c_end = n
        i = 1
        flag = 1
        while i <= n*n:
            if flag % 4 == 1:
                j = c_begin
                while j < c_end:
                    res[r_begin][j] = i
                    i += 1
                    j += 1
                r_begin += 1
                flag += 1
            elif flag % 4 == 2:
                j = r_begin
                while j < r_end:
                    res[j][c_end-1] = i
                    i += 1
                    j += 1
                c_end -= 1
                flag += 1
            elif flag % 4 == 3:
                j = c_end-1
                while j >= c_begin:
                    res[r_end-1][j] = i
                    i += 1
                    j -= 1
                r_end -= 1
                flag += 1
            else:
                j = r_end-1
                while j >= r_begin:
                    res[j][c_begin] = i
                    i += 1
                    j -= 1
                c_begin += 1
                flag += 1
        return res
    
    def generateMatrix0(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for i in range(n)]
        count = 1
        top_left, bottom_right = 0, n-1
        while top_left <= bottom_right:
            res[top_left][top_left:bottom_right+1] = [i + count for i in range(bottom_right - top_left+1)]
            count += bottom_right - top_left
            for i in range(top_left, bottom_right):
                res[i][bottom_right] = count
                count += 1
            res[bottom_right][bottom_right:top_left:-1] = [i + count for i in range(bottom_right - top_left)]
            count += bottom_right - top_left
            for i in range(bottom_right, top_left, -1):
                res[i][top_left] = count
                count += 1
            top_left += 1
            bottom_right -= 1
        return res