class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < len(s):
            res = [s[i] for i in range(numRows)]
        else:
            return s
        if numRows == 1:
            return s
        for i in range(numRows, len(s)):
            c = 2*(numRows - 1)
            t = i % c
            if t in range(numRows):
                res[t] += s[i]
            else:
                res[c-t] += s[i]
        return "".join(res)

    def convert0(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        temp = ['' for i in range(numRows)]
        index = -1
        step = 1
        for i in range(len(s)):
            index += step
            if index == numRows:
                index -= 2
                step = -1
            if index == -1:
                index = 1
                step = 1
            temp[index] += s[i]
        return "".join(temp)