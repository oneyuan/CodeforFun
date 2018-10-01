class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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
        return len(res)
    
    def totalNQueens0(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n < 4:
            return 0
        else:
            return [2, 10, 4, 40, 92, 352, 724, 2680, 14200][n-4]
        # out = []
        # for i in range(2, 13):
        #     out.append(helper(i))
        # print(out)
def helper(n):
    eb = [[False for _ in range(n)] for _ in range(n)]
    rows = set()
    diag = set()
    diagp = set()
    ct = [0]

    def dfs(rn):
        if rn == n:
            ct[0] += 1
        else:
            for i in range(n):
                if (i in rows) or ((i - rn) in diag) or ((n-i - rn) in diagp):
                    continue
                rows.add(i)
                diag.add(i - rn)
                diagp.add(n-i - rn)
                eb[i][rn] = True
                dfs(rn + 1)
                eb[i][rn] = False
                rows.remove(i)
                diag.remove(i - rn)
                diagp.remove(n-i - rn)
    dfs(0)
    return ct[0]