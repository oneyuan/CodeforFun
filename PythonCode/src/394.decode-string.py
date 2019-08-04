#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# first should not just reverse the alphabet because the alpha list isnot store 
# byte it also store string, and digit may be bigger than 10 so should be careful
class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        alpha = []
        slen = len(s)
        i = 0
        while i < slen:
            if s[i] == "]":
                n = len(alpha)
                tmp = []
                while alpha[n-1] != "[":
                    tmp.append(alpha.pop())
                    n -= 1
                alpha.pop()
                tmp.reverse()
                tmp = "".join(tmp)
                alpha.append(int(num.pop())*tmp)
                i += 1
            elif s[i].isdigit():
                tmp = ""
                while s[i].isdigit():
                    tmp += s[i]
                    i += 1
                num.append(tmp)
            else:
                alpha.append(s[i])
                i += 1

        return "".join(alpha)

    def decodeString0(self, s: str) -> str:
        return self.func(s, 0, "")

    def func(self, strng, currIdx, result):
        if currIdx >= len(strng):
            return result

        while currIdx < len(strng) and strng[currIdx].isalpha():
            result += strng[currIdx]
            currIdx += 1

        m = 0
        while currIdx < len(strng) and strng[currIdx].isdigit():
            m = m*10 + int(strng[currIdx])
            currIdx += 1

        # digit will always be followed by open braces
        if m > 0:
            closingbraceIdx = self.findclosingbrace(strng, currIdx)
            result += m*self.func(strng[currIdx+1:closingbraceIdx], 0, "")
            return self.func(strng, closingbraceIdx+1, result)
        else:  # closing braces
            return result

    def findclosingbrace(self, strng, stIdx):
        stk = list()
        while stIdx < len(strng):
            if strng[stIdx] == '[':
                stk.append('[')

            if strng[stIdx] == ']':
                stk.pop()

            if len(stk) == 0:
                return stIdx

            stIdx += 1
        return -1
