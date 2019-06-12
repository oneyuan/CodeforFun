#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
import math
import collections
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

    _dp =  static list to accelerate oj speed
    dp = self._dp
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
'''
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        perfectSquares = []
        cntPerfectSquares = [0 for _ in range(n)]
        i = 1
        while i*i <= n:
            perfectSquares.append(i*i)
            cntPerfectSquares[i*i-1] = 1
            i += 1
        if perfectSquares[-1] == n:
            return 1
        searchQ = collections.deque()
        for k in perfectSquares:
            searchQ.append(k)
        curr = 1
        while searchQ:
            curr += 1
            Qsize = len(searchQ)
            for j in range(Qsize):
                tmp = searchQ[0]
                for l in perfectSquares:
                    if tmp + l == n:
                        return curr
                    elif tmp + l < n and cntPerfectSquares[tmp+l-1] == 0:
                        cntPerfectSquares[tmp+l-1] = curr
                        searchQ.append(tmp+l)
                    elif tmp + l > n:
                        break
                searchQ.popleft()
        return 0
'''



