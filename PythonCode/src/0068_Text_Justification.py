class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        tmp = []
        res = []
        count = 0
        for word in words:
            if len(word) + len(tmp) + count > maxWidth:
                for i in range(maxWidth-count):
                    tmp[i % (len(tmp)-1 or 1)] += " "
                res.append("".join(tmp))
                tmp = []
                count = 0
            tmp.append(word)
            count += len(word)
        res.append(" ".join(tmp).ljust(maxWidth))
        return res
    
    