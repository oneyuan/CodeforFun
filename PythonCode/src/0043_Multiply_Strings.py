class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int_num1, int_num2 = 0, 0
        
        for d in num1:
            int_num1 = int_num1 * 10 + ord(d) - ord('0')
            
        for d in num2:
            int_num2 = int_num2 * 10 + ord(d) - ord('0')
        
        mult = int_num1 * int_num2
        res = []
        
        while len(res) == 0 or mult > 0:
            res.append(chr(ord('0') + mult % 10))
            mult //= 10
        
        return ''.join(res[::-1])
    
    def multiply0(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))