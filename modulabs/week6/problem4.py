class Solution:
    def __init__(self):
        self.max = 0
        
    def islandFinder(self, idx):
        res = 0
        
        if self.visited[idx[0]][idx[1]] or self.grid[idx[0]][idx[1]]==0:
            return 0
        
        self.visited[idx[0]][idx[1]] = True
        
        if idx[1] > 0:
            res += self.islandFinder([idx[0], idx[1]-1]) ## Left
        if idx[1] < len(self.grid[0])-1:
            res += self.islandFinder([idx[0], idx[1]+1]) ## Right
        if idx[0] < len(self.grid)-1:
            res += self.islandFinder([idx[0]+1, idx[1]]) ## Up
        if idx[0] > 0:
            res += self.islandFinder([idx[0]-1, idx[1]]) ## Down
       
        return res + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)): # row
            for j in range(len(grid[0])): # column
                self.max = max(self.max, self.islandFinder([i, j]))
        return self.max