class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        X, Y = len(grid), len(grid[0])
        def dfs(i, j, visited):
            if i < 0 or i >= X or j < 0 or j >= Y or visited[i][j] or grid[i][j]==0:
                return 0
            else:
                visited[i][j]=True
                gold = 0
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    gold = max(gold, dfs(i+x, j+y, visited))
            
            visited[i][j]=False
            
            return grid[i][j]+ gold
        
        
        def degree(i, j):
            deg = 0
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x+=i
                y+=j
                if 0 <= x < X and 0 <= y < Y and grid[x][y]!=0:
                    deg+=1
            return deg
        
        
        ans = 0
        visited = [[False for _ in range(Y)] for _ in range(X)]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and degree(i, j)<=2:
                    ans = max(ans, dfs(i, j, visited))
        return ans