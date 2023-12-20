class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            now=paths[i][1]
            good=True
            for j in range(len(paths)):
                if now==paths[j][0]:
                    good=False
            if good:
                return now
