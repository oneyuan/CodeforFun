class Solution:
    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(t, start, end):
            while end < len(t) and start >= 0 and t[start] == t[end]:
                start -= 1
                end += 1
            return end - start - 1
            
        c = -1
        start = 0
        end = 1
        for i in range(len(s)):
            l1 = isPalindrome(s, i, i)
            l2 = isPalindrome(s, i, i+1)
            l = max(l1, l2)
            if l > c:
                c = l
                start = i-((l-1)//2)
                end = i+1+(l//2)
        return s[start:end]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # res = ""
        # for i in range(len(s)):
        #     temp = ""
        #     for letter in s[i:]:
        #         temp += letter
        #         if temp == temp[::-1] and len(res) < len(temp):
        #             res = temp
        # return res
        
        size = len(s)
        if size <= 1 or s[::-1] == s:
            return s
        start, maxlen = 0, 1
        for idx in range(1, size):
            temp1 = idx - maxlen - 1
            sub2 = s[temp1 : idx + 1]
            if temp1 >= 0 and sub2[::-1] == sub2:
                start = temp1
                maxlen += 2
                continue
            temp2 = idx - maxlen
            sub1 = s[temp2 : idx + 1]
            if temp2 >= 0 and sub1[::-1] == sub1:
                start = temp2
                maxlen += 1
        return s[start : start + maxlen]