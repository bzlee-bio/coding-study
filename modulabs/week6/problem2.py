class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        peopleTrust = [[0 for _ in range(2)] for _ in range(n)]
        
        for t in trust: 
            peopleTrust[t[0]-1][0]+=1
            peopleTrust[t[1]-1][1]+=1
        
        return peopleTrust.index([0,n-1])+1 if [0, n-1] in peopleTrust else -1