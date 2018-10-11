class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        elif n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        if s[1] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(1, n):
            if 10 <= int(s[i-1] + s[i]) <= 26:
                dp[i+1] += dp[i-1]
            if s[i] != "0":
                dp[i+1] += dp[i]
        return dp[n]
    
    