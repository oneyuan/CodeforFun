class Solution:
    def isMatch_1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        firstmatch = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        else: 
            return firstmatch and self.isMatch(s[1:], p[1:])
        
    def isMatch0(self, s, p):
        dp = {}
        dp[(-1,-1)] = True;
        return self.dP(dp,s,p,len(s) - 1,len(p) - 1)
    
    def dP(self,dp,s,p,index1,index2):
        if (index1,index2) in dp:
            return dp[(index1,index2)];
        
        if index1 == -1 and index2 != -1 and p[index2] == '*':
            dp[(index1,index2-2)] = self.dP(dp,s,p,index1,index2-2);
            return dp[(index1,index2-2)];
        
        if index1 < 0 or index2 < 0:
            return False;
        if p[index2] == '.':
            dp[(index1,index2)] = self.dP(dp,s,p,index1-1,index2-1);
            return dp[(index1,index2)];
        if p[index2] == '*':
            if s[index1] == p[index2 - 1] or p[index2 - 1] == '.':
                dp[(index1,index2)] = (self.dP(dp,s,p,index1 - 1, index2) or self.dP(dp,s,p,index1,index2-2));
                return dp[(index1,index2)]
            else:
                dp[(index1,index2)] = self.dP(dp,s,p,index1,index2-2);
                return dp[(index1,index2)]
        if s[index1] != p[index2]:
            dp[(index1,index2)] = False;
            return False;
        else:
            dp[(index1,index2)] = self.dP(dp,s,p,index1-1,index2-1);
            return dp[(index1,index2)] 
    