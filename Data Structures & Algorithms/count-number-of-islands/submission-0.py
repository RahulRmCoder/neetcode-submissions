class Solution:
    def dfs(self, row: int, col: int, grid: List[List[str]], visited: List[List[bool]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
    
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            visited[row][col] or 
            grid[row][col] == '0'):
            return
        
        visited[row][col] = True
        
       
        adjList = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        for r, c in adjList:
            self.dfs(r, c, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        nislands = 0
        visited = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(i, j, grid, visited)
                    nislands += 1
        return nislands
