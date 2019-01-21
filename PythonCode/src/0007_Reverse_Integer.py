class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            neg = 1
            x = -x
        else:
            neg = 0
        s = str(x)
        l = [s[i] for i  in range(len(s))]
        l.reverse()
        res = int("".join(l))
        if neg:
            if res > pow(2, 31):
                return 0
            return -res
        else:
            if res > pow(2, 31)-1:
                return 0
            return res
        
    def reverse0(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            reverse_x = int(str(x)[::-1])
        else:
            reverse_x = -int(str(x)[::-1][:-1])
        
        if -2**31 < reverse_x < 2**31 - 1:
            return reverse_x
        else:
            return 0