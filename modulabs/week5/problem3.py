class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dictChar = dict()
        for c in sentence: # O(N)
            dictChar[c] = 1
            
        return sum(dictChar.values()) == 26