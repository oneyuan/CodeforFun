from heapq import heappush, heappop

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        elif n == 0:
            return m
        if word1 == word2:
            return 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
    
    



    def minDistance0(self, word1, word2, d=0):
        heap = [(0, word1, word2)]
        visited = set()
        while heap:
            d, w1, w2 = heappop(heap)
            if (w1, w2) in visited:
                continue
            visited.add((w1, w2))    
            if w1 == w2:
                return d
            if w1 and w2 and w1[0] == w2[0]:
                heappush(heap, (d, w1[1:], w2[1:]))
            else:
                if w1: heappush(heap, (d+1, w1[1:], w2)) #delete
                if w1 and w2: heappush(heap, (d+1, w1[1:], w2[1:])) #replace
                if w2: heappush(heap, (d+1, w1, w2[1:])) #add

