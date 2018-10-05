class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tmp = []
        t = ""
        i = 1
        while i < len(path):
            if path[i]== "/":
                i += 1
                if t == "..":
                    try:
                        tmp.pop()
                    except:
                        tmp
                elif t == ".":
                    t = ""
                else:
                    if t:
                        t = "/" + t
                        tmp.append(t)
                t = ""
            else:
                t += path[i]
                i += 1
        if t:
            if t == "..":
                try:
                    tmp.pop()
                except:
                    tmp
            elif t == ".":
                t = ""
            else:
                t = "/" + t
                tmp.append(t) 
                t = ""
        if not tmp:
            return ("/")
        return ("".join(tmp))
    
    def simplifyPath0(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths=path.split('/')
        res = []
        for p in paths:
            if(p=='..'):
                if(len(res)>0):
                    res.pop()
            elif(p=='.'):
                continue
            elif(len(p)>0):
                res.append(p)
        s = '/'+'/'.join(res)
        return s