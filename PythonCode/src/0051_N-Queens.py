class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backTrack(n, res, tmp, flag, row):
            if row == n:
                z = []
                for t in tmp:
                    z.append("".join(t))
                res.append(z)
            else:
                for col in range(n):
                    if flag[row] and flag[n+col] and flag[2*n+row+col] and flag[5*n-2+col-row]:
                        tmp[row][col] = "Q"
                        flag[row] = flag[n+col] = flag[2*n+row+col] = flag[5*n-2+col-row] = False
                        backTrack(n, res, tmp, flag, row+1)
                        tmp[row][col] = "."
                        flag[row] = flag[n+col] = flag[2*n+row+col] = flag[5*n-2+col-row] = True
            
        res = []
        flag = [True for _ in range(6*n-2)]
        tmp = [["." for _ in range(n)] for _ in range(n) ]
        backTrack(n, res, tmp, flag, 0)
        return res
    
    def solveNQueens0(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(curr, cols, main_diag, anti_diag, result):
            row, n = len(curr), len(cols)
            if row == n:
                res = []
                for ch in map(lambda x: '.'*x + "Q" + '.'*(n-x-1), curr):
                    res.append(ch)
                result.append(res)
                return
            for i in range(n):
                if cols[i] or main_diag[row+i] or anti_diag[row-i+n-1]:
                    continue
                cols[i] = main_diag[row+i] = anti_diag[row-i+n-1] = True
                curr.append(i)
                dfs(curr, cols, main_diag, anti_diag, result)
                curr.pop()
                cols[i] = main_diag[row+i] = anti_diag[row-i+n-1] = False

        result = []
        cols, main_diag, anti_diag = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        dfs([], cols, main_diag, anti_diag, result)
        return result