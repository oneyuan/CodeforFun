class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = [s[i] for i in range(len(s))]
        l.reverse()
        t = "".join(l)
        if s == t:
            return True
        else:
            return False
        
    def isPalindrome0(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]