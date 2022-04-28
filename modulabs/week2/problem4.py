class Solution:
    def digger(self, digits):
        if len(digits)<=1:
            return list(self.dToL[digits])
        else:
            letterList = self.digger(digits[:-1])
        currLetterList = self.dToL[digits[-1]]
        retLetterList = list()
        for cL in currLetterList:
            retLetterList+=["".join([x,cL]) for x in letterList]
        return retLetterList
        
    def letterCombinations(self, digits: str) -> List[str]:
        self.dToL = {"":"","1":"","2":"abc","3":"def","4":"ghi",\
               "5":"jkl","6":"mno","7":"pqrs","8":"tuv",\
               "9":"wxyz"}
        return self.digger(digits)