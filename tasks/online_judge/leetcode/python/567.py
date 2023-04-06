from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        C = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if s2[i] in s1:
                chk = Counter(s2[i:i+len(s1)])
                if not (C - chk):
                    return True
        return False
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion('ab', 'eidbaooo'))
    print(solution.checkInclusion('abc', 'eidbacooo'))
    print(solution.checkInclusion('abi', 'eidbaooo'))
    print(solution.checkInclusion('adc', 'dcda'))