from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        st = Counter(t)
        return list((st-sc).keys())[0]