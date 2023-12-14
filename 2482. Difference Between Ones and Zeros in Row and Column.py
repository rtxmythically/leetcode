class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        res=grid
        m=len(grid)
        n=len(grid[0])
        oneRow=[0]*n
        oneCol=[0]*m
        zeroRow=[0]*n
        zeroCol=[0]*m
        for row in range(n):
            for col in range(m):
                if grid[col][row]==1:
                    oneRow[row]+=1
                    oneCol[col]+=1
                else:
                    zeroRow[row]+=1
                    zeroCol[col]+=1
        for row in range(n):
            for col in range(m):
                res[col][row]=oneRow[row]+oneCol[col]-zeroRow[row]-zeroCol[col]
        return res

        
