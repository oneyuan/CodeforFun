class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        count = 0
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                count += 1
            else:
                if count != 0:
                    return count
                else:
                    continue
        return count
    
    def lengthOfLastWord0(self, s):
        """
        :type s: str
        :rtype: int
        """
        splt = s.split()
        if splt:
            return len(splt[-1])
        return 0