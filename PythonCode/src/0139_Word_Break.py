class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Time limit exceeded
        """
        n = len(s)
        if n == 0:
            return True
        for i in range(n+1):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False
    
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
    
    def wordBreak0(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        find = [False]*len(s)
        wordDict = set(wordDict)
        maxlength = max(len(w) for w in wordDict)
        for i in range(len(s)):
            for j in range(max(0, i+1-maxlength), i+1):
                if s[j:i+1] in wordDict and (find[j-1] or j < 1):
                    find[i] = True
                    break
        return find[-1]
