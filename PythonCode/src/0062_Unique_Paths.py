class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        dynamic programming
        """
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            res[0][i] = 1
        for j in range(n):
            res[j][0] = 1
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
    
    coor_path_dict = dict()
    
    def uniquePaths0(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m, n) in self.coor_path_dict:
            return self.coor_path_dict[(m, n)]
        
        if m == 1:
            return 1
        if n == 1:
            return 1
        
        r_path = 0 if m == 1 else self.uniquePaths(m-1, n)
        d_path = 0 if n == 1 else self.uniquePaths(m, n-1)
        path = r_path + d_path
        
        self.coor_path_dict[(m, n)] = path
        if m != n:
            self.coor_path_dict[(n, m)] = path
        return path
    
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # only use one array. up is current value of array. left is dp[i - 1.]
        dp = [1 for _ in range(n)] 
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]