class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def subString(t):
            tmp = {}
            for i in range(len(t)):
                if t[i] in tmp:
                    return len(tmp)
                tmp[t[i]] = 1
            return len(tmp)
                
        res = 0
        for i in range(len(s)):
            t = subString(s[i:]) 
            if t > res:
                res = t
        return res
    
    def lengthOfLongestSubstring0(self, s):
        chars = {}
        max_len = 0
        start = 0
        
        for i, c in enumerate(s, 1):
            if c in chars and chars[c] > start:
                start = chars[c]# + 1
            elif i - start > max_len:
                max_len = i - start              
            chars[c] = i
        return max_len