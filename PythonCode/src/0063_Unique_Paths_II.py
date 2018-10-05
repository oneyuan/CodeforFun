class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m > 0:
            n = len(obstacleGrid[0])
        else:
            return 0
        res = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if res[i][j] == -1:
                    if obstacleGrid[i][j] == 1:
                        if i == 0:
                            for k in range(j, n):
                                res[i][k] = 0
                        if j == 0:
                            for k in range(i, m):
                                res[k][j] = 0
                        else:
                            res[i][j] = 0
                    else:
                        if i == 0 or j == 0:
                            res[i][j] = 1
                else:
                    continue
        for i in range(1, m):
            for j in range(1, n):
                if res[i][j] == -1:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
    
    def uniquePathsWithObstacles0(self, obstacleGrid):
        width=len(obstacleGrid[0])
        dp=[0]*width
        dp[0]=1
        
        for row in obstacleGrid:
            for j in range(width):
                if row[j]==1:
                    dp[j]=0
                elif j>0:
                    #注意这一步，加的是dp[j-1]
                    dp[j]+=dp[j-1]
        
        return dp[width-1]
    '''
    def uniquePathsWithObstacles(self, obstacleGrid):
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        
        dp=[0]*col
        if obstacleGrid[0][0]==1:
            dp[0]=0
        else:
            dp[0]=1
        for i in range(1,col):
            if obstacleGrid[0][i]==0:
                dp[i]=dp[i-1]
        for i in range(1,row):
            for j in range(col):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                else:
                    if j>0:
                        dp[j]+=dp[j-1]
        return dp[-1]
    '''
    