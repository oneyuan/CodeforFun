class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        tmp = [strs[0][i] for i in range(len(strs[0]))]
        res = []
        j = 0
        while j < len(tmp):
            for i in strs:
                if j >= len(i) or i[j] != tmp[j]:
                    return "".join(res)
            res.append(tmp[j])
            j += 1
        return strs[0]
    
    def longestCommonPrefix0(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ["flower","flow","flight"] 
        """
        if not strs:
            return ""
        for i,ch in enumerate(zip(*strs)):
            if len(set(ch)) != 1:
                return strs[0][:i]
        else:
            return min(strs,key = len)