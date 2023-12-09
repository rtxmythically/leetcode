class Solution:
    def totalMoney(self, n: int) -> int:
        count=0
        ans=0
        week=n//7
        others=n%7
        for weeks in range(week):
            ans+=(weeks*7+28)
        for other in range(others):
            ans+=(other+week*1+1)
        return ans
