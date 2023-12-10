class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for c in range(len(matrix[0])):
            tmp=[]
            for i in range(len(matrix)):
                tmp.append(matrix[i][c])
            res.append(tmp)
        return res
                
            
                        
        
                       
    