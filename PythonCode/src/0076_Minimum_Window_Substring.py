import collections

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.Counter(t)
        l = 0
        r = 0
        formed = 0
        required = len(dic)
        c = []
        count = {}
        ans = float("inf"), 0, 0
        for i in range(len(s)):
            if s[i] in dic:
                c.append((s[i], i))
        while r < len(c):
            character = c[r][0]
            count[character] = count.get(character, 0) + 1
            if count[character] == dic[character]:
                formed += 1
            while l <= r and formed == required:
                character = c[l][0]
                start = c[l][1]
                end = c[r][1]
                if end - start - 1 < ans[0]:
                    ans = (end-start-1, start, end)
                count[character] -= 1
                if count[character] < dic[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]
    
    def minWindow0(self, s, t):
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        missing = len(t)
        
        MAX = float('inf')
        a, b = 0, MAX
        
        i = 0
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
                
            if missing == 0:
                while need[s[i]] < 0: # Remove unneeded chars from beginning of window
                    need[s[i]] += 1
                    i += 1
                    
                if j - i < b - a:
                    a, b = i, j
                
                need[s[i]] += 1
                missing += 1
                i += 1
        
        return '' if b == MAX else s[a:b]
                    