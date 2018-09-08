class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        t = self.countAndSay(n-1)
        pre = t[0]
        i = 1
        count = 1
        res = ""
        while i < len(t):
            tmp = t[i]
            if tmp == pre:
                count += 1
            else:
                z = str(count) + str(pre)
                res += z
                pre = t[i]
                count = 1
            i += 1
        z = str(count) + str(pre)
        res += z
        return res
    
    def countAndSay0(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s
    