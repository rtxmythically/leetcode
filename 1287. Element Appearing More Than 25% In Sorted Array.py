class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)//4
        x=-1
        c=0
        for i in arr:
            c+=1
            if x==-1:
                x=i
            if x!=i:
                c=1
                x=i
            if c>n:
                return x

            
