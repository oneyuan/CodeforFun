class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        if n == 0:
            return 1
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
    
    def numTrees0(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        seen = {}

        def CountTree(n):
            if n in seen:
                return seen[n]
            if n == 1 or n == 0:
                return 1
            res = 0
            for i in range(n):
                res += CountTree(i)*CountTree(n-1-i)
            seen[n] = res
            return res

        return CountTree(n)
