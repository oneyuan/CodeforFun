import string

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        Tpoint = 0 
        plus = 0
        tmp = []
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        end = 0
        if len(str) == 0:
            return 0
        for i in range(len(str)):
            if str[i] == "+" and plus == 0 and Tpoint == 0:
                plus = 1
                Tpoint = 1
            elif str[i] == "-" and plus == 0 and Tpoint == 0:
                plus = -1
                Tpoint = 1
            elif str[i] == " " and Tpoint == 0:
                continue
            elif str[i].isdigit() and end == 0:
                Tpoint = 1
                tmp.append(str[i])
            else:
                end = 1
                if Tpoint ==0 and str[i] != "+" and str[i] != "-":
                    return 0
        if len(tmp) == 0:
            return 0
        num = int("".join(tmp))
        if plus == 0 or plus == 1:
            if num > INT_MAX:
                return INT_MAX
            else:
                return num
        elif plus == -1:
            if num > -INT_MIN:
                return INT_MIN
            else:
                return -num
            
    def myAtoi0(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        digits = set(string.digits)
        letters = set(string.ascii_letters)
        wspace = set(string.whitespace)

        try:
            num = ''
            for char in str:
                if char in '-+':
                    if not num:
                        num += char
                    else:
                        break
                elif char in digits:
                    num += char
                elif not num and char in wspace:
                    continue
                else:
                    break
            res = int(num)
            if res > INT_MAX:
                return INT_MAX
            elif res < INT_MIN:
                return INT_MIN
            return res
        except:
            return 0