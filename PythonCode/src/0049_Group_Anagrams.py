class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        tmp = []
        dic = {}
        for word in strs:
            for i in range(len(word)):
                if word[i] in dic:
                    dic[word[i]] += 1
                else:
                    dic[word[i]] = 1
            if dic in tmp:
                index = tmp.index(dic)
                res[index].append(word)
            else:
                t = dic.copy()
                tmp.append(t)
                res.append([word])
            dic = {}
        return res

    def groupAnagrams0(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 
        if len(strs) == 0:
            return None
        mydict = {}
        for s in strs:
            a = list(s)
            a.sort()
            a = "".join(a)
            if a in mydict:
                mydict[a].append(s)
            else:
                mydict[a] = [s]
        
        
        return list(mydict.values())  
                        
    