class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tmp = []
        if num // 1000 :
            m = num // 1000
            num -= m*1000
            for i in range(m):
                tmp.append("M")
        if num // 900:
            num -= 900
            tmp.append("CM")
        elif num // 500:
            num -= 500
            tmp.append("D")
            if num // 100:
                c = num // 100
                num -= c*100
                for i in range(c):
                    tmp.append("C")
        elif num // 400:
            num -= 400
            tmp.append("CD")
            if num // 100:
                c = num // 100
                num -= c*100
                for i in range(c):
                    tmp.append("C")
        else:
            c = num // 100
            num -= c*100
            for i in range(c):
                tmp.append("C")
        if num // 90:
            num -= 90
            tmp.append("XC")
        elif num // 50:
            num -= 50
            tmp.append("L")
            if num // 10:
                x = num // 10
                num -= x*10
                for i in range(x):
                    tmp.append("X")
        elif num // 40:
            num -= 40
            tmp.append("XL")
            if num // 10:
                x = num // 10
                num -= x*10
                for i in range(x):
                    tmp.append("X")
        else:
            x = num // 10
            num -= x*10
            for i in range(x):
                tmp.append("X")
        if num // 9:
            num -= 9
            tmp.append("IX")
        elif num // 5:
            num -= 5
            tmp.append("V")
            if num // 1:
                i = num // 1
                num -= i*1
                for i in range(i):
                    tmp.append("I")
        elif num // 4:
            num -= 4
            tmp.append("IV")
            if num // 1:
                i = num // 1
                num -= i*1
                for i in range(i):
                    tmp.append("I")
        else:
            i = num // 1
            num -= i*1
            for i in range(i):
                tmp.append("I")
        return "".join(tmp)
    
    def intToRoman0(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanList = ["","I","II","III","IV","V","VI","VII","VIII","IX"
                     ,"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"
                     ,"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"
                     ,"","M","MM","MMM"]
        romanNumString = ""
        position = 0
        while num:
            romanNumString = romanList[(num % 10) + (position * 10)] + romanNumString
            num = num // 10
            position += 1
        return romanNumString