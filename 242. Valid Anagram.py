class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(s):
            ans=[0]*26
            