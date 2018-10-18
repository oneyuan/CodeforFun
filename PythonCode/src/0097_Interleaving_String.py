class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                elif j == 0:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                else:
                    dp[i][j] = ((dp[i-1][j] and s1[i-1] == s3[i+j-1])
                                or (dp[i][j-1] and s2[j-1] == s3[i+j-1]))
        return dp[m][n]
    
    def isInterleave0(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        initial = (0, 0, 0)
        queue = [initial]
        visited = set([])
        while queue:
            state = queue.pop(0)
            if state == (len(s1), len(s2), len(s3)):
                return True
            
            if state[0] < len(s1):
                if s1[state[0]] == s3[state[2]]:
                    new_state = (state[0] + 1, state[1], state[2] + 1)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                
            if state[1] < len(s2):
                if s2[state[1]] == s3[state[2]]:
                    new_state = (state[0], state[1] + 1, state[2] + 1)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
        return False
