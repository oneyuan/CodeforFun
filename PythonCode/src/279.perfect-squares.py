#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
import math
class Solution:
    '''
    dynamic programming
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]
    '''
    def numSquares(self, n: int) -> int:
        def isSquare(n):
            m = math.sqrt(n)
            if m == int(m):
                return True

        if isSquare(n):
            return 1
        #  The result is 4 if and only if n can be written in the
        #  form of 4^k*(8*m + 7). Please refer to
        #  Legendre's three-square theorem.
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        #  Check whether 2 is the result.
        sqrtn = int(math.sqrt(n))
        for i in range(sqrtn+1):
            if isSquare(n-i*i):
                return 2
        return 3

