class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(t):
            if 0 < len(t) < 4 and int(t) < 256:
                if len(t) == 1 and int(t) == 0:
                    return True
                elif t[0] != "0":
                    return True
            return False

        n = len(s)
        res = []
        if n > 12 or n < 4:
            return res
        for i in range(3):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if check(s[:i+1]) and check(s[i+1:j+1]) and check(s[j+1:k+1]) and check(s[k+1:]):
                        res.append(s[:i+1] + "." + s[i+1:j+1] +
                                   "." + s[j+1:k+1] + "." + s[k+1:])
        return res
    
    def restoreIpAddresses0(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        def extend(curr, rem, l):
            # print(curr, rem, l)
            if rem == '' and l == 0:
                ans.append('.'.join(curr))
                return
            if not l <= len(rem) <= 3 * l:
                return
            for i in range(1, min(4, len(rem) + 1)):
                if int(rem[:i]) <= 255 and (rem[:i] == '0' or rem[0] != '0'):
                    # print(rem)
                    extend(curr + [rem[:i]], rem[i:], l-1)

        extend([], s, 4)
        return ans
