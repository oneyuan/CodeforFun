class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        starIndex = -1
        while j < len(s):
            if i < len(p) and (p[i] == "?" or s[j] == p[i]):
                i += 1
                j += 1
            elif i < len(p) and p[i] == "*":
                starIndex = i
                match = j
                i += 1
            elif starIndex != -1:
                i = starIndex + 1
                match += 1
                j = match
            else:
                return False
        while i < len(p) and p[i] == "*":
            i += 1
        return i == len(p)
    
    def isMatch0(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        s_idx, p_idx = 0, 0
        s_start, p_start = 0, -1
        while s_idx < m:
            if p_idx < n and (s[s_idx] == p[p_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            elif p_idx < n and p[p_idx] == '*':
                s_start = s_idx
                p_start = p_idx
                p_idx += 1
            elif p_start != -1:
                s_start += 1
                s_idx = s_start
                p_idx = p_start + 1
            else:
                return False
        while p_idx < n and p[p_idx] == '*':
            p_idx += 1
        return s_idx == m and p_idx == n