class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = [0]
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if dp[i][j] and dp[i+1][j] and dp[i][j+1]:
                        dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    else:
                        dp[i+1][j+1] = 1
                    res.append(dp[i+1][j+1])
        return max(res)*max(res)
        
    
    def maximalSquare0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1 and i and j:
                    matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]) + 1
                    
        return max(map(max, matrix)) ** 2