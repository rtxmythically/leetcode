#暴力破解
#先找到1然後找同一列和同一行有沒有一樣的,要注意r!=row和c!=column不能相同的位址
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=0
        m=len(mat)
        n=len(mat[0])
        for row in range(m):
            for column in range(n):
                if mat[row][column]==0:
                    continue
                good=True
                for c in range(n):
                    if c!=column and mat[row][c]==1:
                        good=False
                        break
                for r in range(m):
                    if r!=row and mat[r][column]==1:
                        good=False
                        break
                if good:
                    ans+=1
        return ans
    #--------------------------------------------------------
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=0
        m=len(mat)
        n=len(mat[0])
        row_count=[0]*m
        column_count=[0]*n
        for row in range(m):
            for column in range(n):
                if mat[row][column]==1:
                    row_count[row]+=1
                    column_count[column]+=1
        for row in range(m):
            for column in range(n):
                if mat[row][column]==1:
                    if row_count[row]==1 and column_count[column]==1:
                        ans+=1
        return ans
                                        
            
                        
            
                    


