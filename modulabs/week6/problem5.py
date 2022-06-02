from collections import defaultdict

class Solution:
    def dfs(self, i):
        self.visited[i] = True
        self.c.append(self.s[i])
        self.idx.append(i)
        
        for node in self.nodeConnect[i]:
            if not self.visited[node]:
                self.dfs(node)
        
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.nodeConnect = defaultdict(list)
        self.s = s
        s = list(s)
        self.visited = [False for _ in range(len(s))]
        
        for n1, n2 in pairs:
            self.nodeConnect[n1].append(n2)
            self.nodeConnect[n2].append(n1) ## bidirectional

        for i in range(len(s)):
            if not self.visited[i]:
                self.c = list()
                self.idx = list()
                
                self.dfs(i)
                
                self.c = sorted(self.c)
                self.idx = sorted(self.idx)
                for _c, _i in zip(self.c, self.idx):
                    s[int(_i)] = _c
                    
        return "".join(s)

