class Solution:
    def searchPalindrome(self, s):
        p = 0
        q = len(s)-1
        
        while p<q:
            if s[p] != s[q]:
                return False, p, q
            else:
                p+=1
                q-=1
        return True, None, None
        
    def validPalindrome(self, s: str) -> bool:
        res, p, q = self.searchPalindrome(s)
        if res:
            return True
        else:
            res, _, _ = self.searchPalindrome(s[p+1:q+1]) ## left jump
            if res:
                return True
            res, _, _ = self.searchPalindrome(s[p:q]) ## right jump
            if res:
                return True
        return False