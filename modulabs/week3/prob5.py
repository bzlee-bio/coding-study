class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        pLen = len(p)
        res = list()
        
        for i in range(len(s)-len(p)+1):
            if p == sorted(s[i:i+pLen]):
                res.append(i)
        return res