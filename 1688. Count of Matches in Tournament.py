class Solution:
    def numberOfMatches(self, n: int) -> int:
        matchtimes=int(n/2)
        ans=0
        nextmatch=0
        while matchtimes>0:
            if n==3:
                matchtimes+=1
            nextmatch=int((n-1)/2)+1
            ans+=n-nextmatch
            n=nextmatch
            matchtimes-=1
        return ans
    