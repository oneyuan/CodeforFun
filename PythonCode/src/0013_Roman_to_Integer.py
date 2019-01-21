class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}
        res = 0
        for i in range(len(s)):
            d[s[i]] += 1
        i = 0
        while i < len(s):
            if s[i] == "M":
                res += 1000
                d["M"] -= 1
                i += 1
            elif s[i] == "C":
                if d["M"] == 0 and d["D"] == 0:
                    res += 100
                    i += 1
                else:
                    if d["M"] != 0:
                        res += 900
                        d["M"] -= 1
                    elif d["D"] != 0:
                        d["D"] -= 1
                        res += 400
                    i += 2
                d["C"] -= 1
            elif s[i] == "X":
                if d["C"] == 0 and d["L"] == 0:
                    res += 10
                    i += 1
                else:
                    if d["C"] != 0:
                        res += 90
                        d["C"] -= 1
                    elif d["L"] != 0:
                        res += 40
                        d["L"] -= 1
                    i += 2
                d["X"] -= 1
            elif s[i] == "I":
                if d["V"] == 0 and d["X"] == 0:
                    res += 1
                    i += 1
                else:
                    if d["V"] != 0:
                        res += 4
                        d["V"] -= 1
                    elif d["X"] != 0:
                        res += 9
                        d["X"] -= 1
                    i += 2
                d["I"] -= 1
            elif s[i] == "D":
                res += 500
                d["D"] -= 1
                i += 1
            elif s[i] == "L":
                res += 50
                d["L"] -= 1
                i += 1
            elif s[i] == "V":
                res += 5
                d["V"] -= 1
                i += 1
        return res
    
    roman_to_int_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt0(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        pre_val = float('inf')
        for c in s:
            val = Solution.roman_to_int_mapping[c]
            if val > pre_val:
                result -= 2 * pre_val
            pre_val = val
            result += val
        return result