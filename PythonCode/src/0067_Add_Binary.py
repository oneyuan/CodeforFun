class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == "1" and b[-1] == "1":
            s = self.addBinary(self.addBinary(a[:-1], b[:-1]), "1" ) + "0"
        elif a[-1] == "1" or b[-1] == "1":
            s = self.addBinary(a[:-1], b[:-1]) + "1"
        else:
            s = self.addBinary(a[:-1], b[:-1]) + "0"
        return s
    
    def addBinary0(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        su = str(bin(int(a,2) + int(b,2)))
        return su[2:]
    
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a: return b
        if not b: return a
        res = []
        carry = 0
        
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            sums = carry
            if i >= 0: sums += int(a[i])
            if j >= 0: sums += int(b[j])
            res.insert(0, str(sums % 2))
            carry = sums//2
            i-=1
            j-=1
            
        """
        while i>=0:
            sums = int(a[i]) + carry
            res.insert(0, str(sums % 2))
            carry = sums//2
            i-=1
            
        while j>=0:
            sums = int(b[j]) + carry
            res.insert(0, str(sums % 2))
            carry = sums//2
            j-=1
        """
            
        if carry: res.insert(0, str(1))
        return "".join(res)
            
        