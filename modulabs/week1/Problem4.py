class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        sol = list()
        for w in words:
            d = dict()
            flag = True
            for s, p in zip(w, pattern):
                if not p in d.keys() and s not in d.values():
                    d[p]=s
                elif not p in d.keys() and s in d.values():
                    flag = False
                    break
                elif d[p]!=s:
                    flag = False
                    break
            if flag:
                sol.append(w)
        
        return sol